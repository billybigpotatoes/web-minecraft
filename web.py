from bottle import route, run
from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

@route('/jump')
def hello():
    position = mc.player.getTilePos()
    x = position.x
    y = position.y
    z = position.z
    mc.player.setTilePos(x,y+20,z)
    return "Jumped!"

@route('/')
def index():
    return "Index"


run(host='0.0.0.0', port=8080, debug=True)
