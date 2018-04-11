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
# for i in range(robot.numLinks()):
#     print i, robot.link(i).getName()

#Generate some waypoint configurations using the resource editor
qi = [0]*60
# qi[15:23] = [-0.62548, -0.09472, -0.69528, 0.49663, 0.94378, 0.0, 0.50161, -0.32789]
qi[15:23] = [-1.06803, 0.02800, -0.51618, 0.02569, 0.71867, 0.0, 0.88166, -0.38503]
# qi[35:43] = [0.67649, -0.13346, 0.30334, 0.59058, -0.55147, 0.0, 0.15532, 0.18139]
qi[35:43] = [1.14473, -0.39884, -0.07478, 0.84752, -0.40229, 0.0, 0.39193, 0.55607]
# qi[55] =

# 54 left_gripper:base
# 55 left_gripper:finger1
# 56 left_gripper:finger2
# 57 right_gripper:base
# 58 right_gripper:finger1
# 59 right_gripper:finger2


robot.setConfig(qi)

vis.add("world",world)
vis.show()

t0 = time.time()
while vis.shown():
    t1 = time.time()
    #update your code here
    time.sleep(max(0.01-(t1-t0),0.001))
    t0 = t1
