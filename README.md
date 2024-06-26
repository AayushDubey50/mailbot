# Mailbot Simulation

## Overview

This portfolio is a simple navigation simulator of a custom robot called 'mailbot'. Mailbot is serviced to deliver mail to a designated location using a pre-saved map of the world environment and a LiDAR sensor to get through its path. It has been developed in the ROS framework (Melodic distribution), Gazebo simulator and RViz visualizer to help the bot navigate through the environment that it's in and find a viable path from start to end goals. A user can launch a ROS world, control the bot's movements around the world using the keyboard, create and save a map of the world, and then navigate with the mailbot.

## Installation:

### Dependencies

- [Robot Operating System (ROS) Melodic Morenia](http://wiki.ros.org/melodic)
- [Ubuntu 18.04.6 LTS](https://releases.ubuntu.com/18.04/)
- [CMake 2.8.3](https://cmake.org/)

### ROS Packages

- [gmapping](http://wiki.ros.org/gmapping)
- [teleop_twist_keyboard](http://wiki.ros.org/teleop_twist_keyboard)
- [map_server](http://wiki.ros.org/map_server)
- [rviz](http://wiki.ros.org/rviz)
- [gazebo_ros](http://wiki.ros.org/gazebo_ros)


## Simulation Instructions

### Creating a map
There should be three separate terminals to create and save a map. One is for OpenSlam's Gmapping package, another for operating the bot's movements, and the third for saving the map.
1. gmapping:
```
roslaunch mailbot_navigation gmapping.launch
```
Params:
* myWorld:=(example world filename in ROS package)
* x:=[float number]
* y:=[float number]
* z:=[float number]
* roll:=[radians]
* pitch:=[radians]
* yaw:=[radians]

2. teleop_twist_keyboard
```
  roslaunch mailbot_control teleop.launch
```
3. map_server (check the YAML file generated and make sure the correct PGM filename is used, such as 'cafe.pgm')
```
  cd ~/src/mailbot_navigation/maps/ ;
  rosrun map_server map_saver -f (example world filename in ROS package)
```

### Navigation in a world
Be sure to run the navigation after a gmapping of the example world you wish to use.
1. navigation:
```
  roslaunch mailbot_navigation navigation.launch
```
Params:
* myWorld:=(example world filename in ROS package)
* x:=[float number]
* y:=[float number]
* z:=[float number]
* roll:=[radians]
* pitch:=[radians]
* yaw:=[radians]

Make sure that the 2D Pose Estimate in RViz is being used to approximate the position and orientation of the mailbot. Then, you can use the 2D Nav Goal in RViz to command the mailbot to set on course its path.

### Viewing the mailbot
1. To spawn the mailbot in an empty world, run the below command in a terminal
```
  roslaunch mailbot_description spawn.launch
```
2. To view the mailbot in RViz:
```
  roslaunch mailbot_description rviz.launch
```
