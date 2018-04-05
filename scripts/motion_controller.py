#!/usr/bin/python

# Motion Controller

""" IMPORT MODULES """
import sys, struct, time, json

sys.path.insert(0, "/home/saeed/Klampt/iml-internal/Ebolabot")

#-----------------------------------------------------------
#Imports require internal folders

from Motion import motion
from Motion import config

#================================================================
# End of Imports


#============================================================
# configuration variables

MODEL_DIR = "/home/saeed/Klampt/data/robots/"
LIBMOTION_DIR = "/home/saeed/catkin_ws/src/klampt/misc/"
KLAMPT_MODEL = "baxter_col.rob"

#============================================================
# paths/directories variables

if __name__ == "__main__":
    """The main loop that loads the planning / simulation models and
    starts the OpenGL visualizer."""
    print 'motion_controller runs!'

    robot_model = MODEL_DIR+KLAMPT_MODEL
    print robot_model

    # Connect to Baxter
    robot = motion.setup(
        mode="physical", \
        libpath=LIBMOTION_DIR, \
        klampt_model= MODEL_DIR+KLAMPT_MODEL)
    res = robot.startup()
    if not res:
        print "Error connecting to robot"
        exit()
