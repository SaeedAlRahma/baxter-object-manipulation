#!/usr/bin/env python
import rospy, time, sys

from klampt.plan import robotcspace
from klampt.plan import cspace
from klampt.plan import robotplanning
from klampt.math import se3
from klampt import vis
from klampt.io import resource
from klampt.model import ik
from klampt.model import trajectory
from klampt.model.collide import WorldCollider
from klampt import *

WS_ROOT = "/home/saeed/catkin_ws/src/klampt"
WORLD_DIR = "/resources/robotWorld.xml"
fn = WS_ROOT + WORLD_DIR
world = WorldModel()
res = world.readFile(fn)
if not res:
    print "Unable to read file",fn
    exit(0)

robot = world.robot(0)

#Generate some waypoint configurations using the resource editor
qi = [0]*60
qi[15:23] = [-0.62548, -0.09472, -0.69528, 0.49663, 0.94378, 0.0, 0.50161, -0.32789]
qi[35:43] = [0.67649, -0.13346, 0.30334, 0.59058, -0.55147, 0.0, 0.15532, 0.18139]


robot.setConfig(qi)

vis.add("world",world)
vis.show()

t0 = time.time()
while vis.shown():
    t1 = time.time()
    #update your code here
    time.sleep(max(0.01-(t1-t0),0.001))
    t0 = t1
