# baxter-object-manipulation
ROS package to test object manipulation using a baxter with klamp't library

## Introduction
This is a ROS package used to test object manipulation on a physical Baxter using klamp't library. I used ROS indigo on ubuntu 14.04.4 LTS but the package should work on any version (not tested).

## Setup
* Follow this [link](http://wiki.ros.org/ROS/Installation) to install and setup ROS (skip if ROS already installed)

* Follow this [link](http://motion.pratt.duke.edu/klampt/#install) to install and setup Klampt library

* Follow this [link](http://sdk.rethinkrobotics.com/wiki/Baxter_Setup) to install and setup baxter

* Make sure to source the setup.bash file on every terminal (if not already done so)

`$ source /opt/ros/<distro>/setup.bash`

* Create a catkin workspace

`$ mkdir -p ~/catkin_ws/src`

`$ cd ~/catkin_ws/`

`$ catkin_make`

* Source your new setup.bash file

`$ cd ~/catkin_ws/`

`$ source devel/setup.bash`

* Create a new package folder

`$ cd ~/catkin_ws/src`

* Clone the files of this repository

`$ git clone https://github.com/SaeedAlRahma/baxter-object-manipulation.git`

* Rename the folder from 'baxter-object-manipulation' to 'baxter_saeed'

* Change the line "SET(KLAMPT_ROOT /home/saeed/Klampt)" in CMakeLists.txt to the Klampt library path on your system

## Run
