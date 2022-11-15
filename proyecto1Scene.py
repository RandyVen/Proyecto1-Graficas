from gl import Render
from obj import Texture
from collections import namedtuple
from math import pi
import random

V2 = namedtuple('Point2', ['x', 'y'])
V3 = namedtuple('Point3', ['x', 'y', 'z'])

r = Render()
r.glInit(1000,1000)

r.lookAt(V3(1, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
r.load('./sphere.obj', translate=(9,24,30), scale=(1.1,1,1.1), rotate=(0,0,0))
r.drawArrays('SHADER')


r.load('./sphere.obj', translate=(6,-3,6), scale=(0.1,0.1,0.1), rotate=(0,0,0))
r.drawArrays('SHADER')

r.load('./sphere.obj', translate=(5,0,6), scale=(0.1,0.1,0.1), rotate=(0,0,0))
r.drawArrays('SHADER')

r.load('./sphere.obj', translate=(4,-1,2), scale=(0.038,0.038,0.038), rotate=(0,0,0))
r.drawArrays('SHADER')

r.load('./sphere.obj', translate=(3,-1,2), scale=(0.03,0.03,0.03), rotate=(0,0,0))
r.drawArrays('SHADER')

r.load('./sphere.obj', translate=(4,-1,6), scale=(0.085,0.085,0.085), rotate=(0,0,0))
r.drawArrays('SHADER')

r.load('./sphere.obj', translate=(4,0,8), scale=(1,1,1), rotate=(0,0,0))
r.drawArrays('SHADER')



r.light = V3(0,0,1)
r.lookAt(V3(1, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
r.load('./merc.obj', translate=(8.2, 7, 10), scale=(1.2, 1.3, 1.3), rotate=(0,4*pi/5,pi))
r.drawArrays('GREYSHADER')

r.load('./Ash.obj', translate=(7.8, 4, 10), scale=(1.2, 1.3, 1.3), rotate=(0,4*pi/5,pi))
r.drawArrays('GREYSHADER')

r.load('./diamond.obj', translate=(0.5, 18, 20), scale=(2, 2, 1), rotate=(0,1,pi/2))
r.drawArrays('GREYSHADER')

t = Texture('./golf_fairway.bmp')
r.texture = t
r.load('./Ivy.obj', translate=(250, 0, 135), scale=(50, 50, 70), rotate=(pi, 0, 0))
r.drawArrays('TRIANGLE')

r.glFinish('proyectoScene.bmp')