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


#settings
KLAMPT_ROOT = "/home/saeed/Klampt"
MODEL_DIR = "/data/robots/baxter_with_parallel_gripper_col.rob"

#global
global world
global robot

def baxter_planner(qi, q, qSubset, settings):
    global world
    global robot

    t0 = time.time()
    print "Creating plan..."
    #this code uses the robotplanning module's convenience functions
    robot.setConfig(qi)
    print 'len(q)', len(q)
    plan = robotplanning.planToConfig(world,robot,q,
                                  movingSubset=qSubset,
                                  **settings)

    if plan is None:
        print 'plan is None...'
        return None

    print "Planner creation time",time.time()-t0
    t0 = time.time()
    plan.space.cspace.enableAdaptiveQueries(True)
    print "Planning..."
    for round in range(100):
        plan.planMore(50)
    print "Planning time, 500 iterations",time.time()-t0

    #this code just gives some debugging information. it may get expensive
    #V,E = plan.getRoadmap()
    #print len(V),"feasible milestones sampled,",len(E),"edges connected"
    path = plan.getPath()
    if path is None or len(path)==0:
        print "Failed to plan path between configuration"
        print qi
        print "and"
        print q
        # #debug some sampled configurations
        # print V[0:min(10,len(V))]

    """
        print "Constraint testing order:"
        print plan.space.cspace.feasibilityQueryOrder()
        print "Manually optimizing constraint testing order..."
        plan.space.cspace.optimizeQueryOrder()
        print "Optimized constraint testing order:"
        print plan.space.cspace.feasibilityQueryOrder()

        print "Plan stats:"
        print plan.getStats()

        print "CSpace stats:"
        print plan.space.getStats()
    """
    #to be nice to the C++ module, do this to free up memory
    plan.space.close()
    plan.close()

    return path


#load the robot / world file
fn = KLAMPT_ROOT + MODEL_DIR
world = WorldModel()
res = world.readFile(fn)
if not res:
    print "Unable to read file",fn
    exit(0)

robot = world.robot(0)

#add the world elements individually to the visualization
vis.add("robot",robot)
print "Added robot to vis"
for i in range(1,world.numRobots()):
    vis.add("robot"+str(i),world.robot(i))
    print "Added robot ", str(i)
for i in range(world.numRigidObjects()):
    vis.add("rigidObject"+str(i),world.rigidObject(i))
    print "Added rigidObject ", str(i)
for i in range(world.numTerrains()):
    vis.add("terrain"+str(i),world.terrain(i))
    print "Added terrain ", str(i)


#Automatic construction of space
space = robotplanning.makeSpace(world=world,robot=robot,
                                edgeCheckResolution=1e-3,
                                movingSubset='all')
print "space ", space

#Generate some waypoint configurations using the resource editor
qi = [0]*60
q1 = list(qi); q1[35:43] = [1.70168, 0.0, -1.34, 0.59, -1.019, 0.0, -0.96, 0.0]
q2 = list(q1); q2[15:23] = [-0.38, 0.0, -0.74582, 1.39, 0.92, 0.0, 0.0, 0.0]
q3 = list(q2); q3[15:23] = [-0.38, 0.0, -2.28582, 1.35, 0.92, 0.0, 0.0, 0.0]

# q1 = list(qi); q1[38] = 0.9; q1[36] = -1;
# q2 = list(q1); q2[41] = -1.35
# q3 = list(q2); q3[18] = 0.9
# q4 = list(q3); q4[16] = -0.7
configs = [qi, q1, q2]#, q3]#, q4]
print "len(configs):", len(configs)
print "Configs:"
for q in configs:
    print "  ", q

#set up a settings dictionary here.  This is a random-restart + shortcutting
#SBL planner.
settings = { 'type':"sbl", 'perturbationRadius':0.5, 'bidirectional':1, 'shortcut':1, 'restart':1, 'restartTermCond':"{foundSolution:1,maxIters:1000}" }

#This code generates a PRM with no specific endpoints
#plan = cspace.MotionPlan(space, "prm", knn=10)
#print "Planning..."
#plan.planMore(500)
#V,E = plan.getRoadmap()
#print len(V),"feasible milestones sampled,",len(E),"edges connected"


#Generate a path connecting the edited configurations
#You might edit the value 500 to play with how many iterations to give the
#planner.
wholepath = [configs[0]]
for i in range(len(configs)-1):
    path = baxter_planner(configs[i], configs[i+1], 'all', settings)
    if path is None or len(path)==0:
        break;
    wholepath += path[1:]

# Move from qi to qf
if len(wholepath)>1:
    print "Path:"
    for q in wholepath:
        print "     Right Arm:", q[35:42+1]
        print "     Left Arm:", q[15:22+1]
        print "---------------"
    #if you want to save the path to disk, uncomment the following line
    #wholepath.save("test.path")

    #draw the path as a RobotTrajectory (you could just animate wholepath, but for robots with non-standard joints
    #the results will often look odd).  Animate with 5-second duration
    times = [i*5.0/(len(wholepath)-1) for i in range(len(wholepath))]
    print "times", times
    traj = trajectory.RobotTrajectory(robot,times=times,milestones=wholepath)
    print traj
    print traj.interpolate(wholepath[0], wholepath[1], 10, 1)
    #show the path in the visualizer, repeating for 60 seconds
    vis.animate("robot",traj)
    vis.spin(60)
else:
    print "Failed to generate a plan"

vis.kill()
