# baxter-object-manipulation
ROS package to test object manipulation using a baxter with klamp't library

## Introduction
This is a ROS package used to test object manipulation on a physical Baxter using klamp't library. I used ROS kinetic on ubuntu 16.04 LTS but the package should work on older versions (not tested).

## Setup
* Follow this [link](http://wiki.ros.org/ROS/Installation) to install ROS (skip if ROS already installed)

* Make sure to source the setup.bash file (if not already done so)

`$ source /opt/ros/<distro>/setup.bash`

* Create a catkin workspace

`$ mkdir -p ~/catkin_ws/src`

`$ cd ~/catkin_ws/`

`$ catkin_make`

* Source your new setup.bash file

`$ cd ~/catkin_ws/`

`$ source devel/setup.bash`

* Create a ROS package

`$ cd ~/catkin_ws/src`

`$ catkin_create_pkg klampt std_msgs rospy roscpp`

`$ cd ~/catkin_ws`

`$ catkin_make`

* Add the workspace to your ROS environment

`$ cd ~/catkin_ws`

`$ . ~/catkin_ws/devel/setup.bash`

* Clone this repository

`$ git clone https://github.com/SaeedAlRahma/baxter-object-manipulation.git`

## Run
