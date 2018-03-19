#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
#from baxter_core_msgs.msg import JointCommand

global joint_cmd_pub

def joint_states_callback(data):
    rospy.loginfo(data)
    #jointCmd = JointCommand()
    jointCmd = JointState()
    global joint_cmd_pub
    joint_cmd_pub.publish(jointCmd)

def baxter_controller():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('baxter_controller', anonymous=True)

    global joint_cmd_pub
    #pub = rospy.Publisher('/test/joint_cmd', JointCommand, queue_size=10)
    joint_cmd_pub = rospy.Publisher('/test/joint_cmd', JointState, queue_size=10)
    rospy.Subscriber("/test/joint_states", JointState, joint_states_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        baxter_controller()
    except rospy.ROSInterruptException:
        pass

