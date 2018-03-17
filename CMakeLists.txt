cmake_minimum_required(VERSION 2.8.3)
project(klampt)

# ADDED #
SET(KLAMPT_ROOT /home/saeed/Klampt)
SET(CMAKE_MODULE_PATH "${KLAMPT_ROOT}/CMakeModules")

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

# ADDED #
FIND_PACKAGE(Klampt REQUIRED)
ADD_DEFINITIONS(${KLAMPT_DEFINITIONS})

add_message_files(
  FILES
  Baxter_Arms.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS message_runtime
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

# ADDED #
include_directories(
  ${KLAMPT_INCLUDE_DIRS}
)

# ADDED #
ADD_EXECUTABLE(MySim src/publisher.cpp)

# ADDED #
TARGET_LINK_LIBRARIES(MySim ${KLAMPT_LIBRARIES})

add_executable(robot_publisher src/robot_publisher.cpp)
target_link_libraries(robot_publisher ${catkin_LIBRARIES})
add_dependencies(robot_publisher klampt_generate_messages_cpp)

add_executable(planner src/planner.cpp)
target_link_libraries(planner ${catkin_LIBRARIES})
add_dependencies(planner klampt_generate_messages_cpp)
