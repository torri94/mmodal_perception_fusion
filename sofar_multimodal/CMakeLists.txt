cmake_minimum_required(VERSION 2.8.3)
project(sofar_multimodal)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

## Generate messages in the 'msg' folder
 add_message_files(
    FILES 
    adapter.msg
    feature.msg
    obj.msg
    TrackedShape.msg
    TrackedShapes.msg
    TensorOutput.msg
    commonFeature.msg
    selectorMatcher.msg
	  outputReasoner.msg        
	  corr.msg
	  correlationTable.msg      
	  record.msg
	  outputReasoner.msg        
    matcherObj.msg     
  )

## Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
   std_msgs
 )


## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)
