#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
#from baxter_core_msgs.msg import JointCommand

def joint_cmd_callback(data):
    rospy.loginfo(data)

def robot_publisher():
    rospy.init_node('robot_publisher', anonymous=True)
    pub = rospy.Publisher('/test/joint_states', JointState, queue_size=10)
    rate = rospy.Rate(1) # 10hz
    #rospy.Subscriber("/test/joint_cmd", JointCommand, joint_cmd_callback)
    rospy.Subscriber("/test/joint_cmd", JointState, joint_cmd_callback)
    while not rospy.is_shutdown():
	jointMsg = JointState()
        #rospy.loginfo(jointMsg)
        pub.publish(jointMsg)
        rate.sleep()

if __name__ == '__main__':
    try:
        robot_publisher()
    except rospy.ROSInterruptException:
        pass

