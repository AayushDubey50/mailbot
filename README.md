# Mailbot Simulation

## Overview

This portfolio is a simple navigation simulator of a custom robot called 'mailbot'. Mailbot is serviced to deliver mail to a designated location using a pre-saved map of the world environment and a LiDAR sensor to get through its path. It has been developed in the ROS framework (Melodic distribution), Gazebo simulator and RViz visualizer to help the bot navigate through the environment that it's in and find a viable path from start to end goals. A user can launch a ROS world, control the bot's movements around the world using the keyboard, create and save a map of the world, and then navigate with the mailbot.

## Installation:

### Dependencies

- [Robot Operating System (ROS) Melodic Morenia](http://wiki.ros.org/melodic)
- [CMake](https://cmake.org/) Version: 3.10.2+
- [Ubuntu 18.04.6 LTS] https://releases.ubuntu.com/18.04/

### ROS Packages

- [gmapping](http://wiki.ros.org/gmapping)
- [teleop_twist_keyboard](http://wiki.ros.org/teleop_twist_keyboard)
- [map_server](http://wiki.ros.org/map_server)


## Simulation Instructions

- Creating a map
There should be three separate terminals to create and save a map. One is for OpenSlam's Gmapping package, another for operating the bot's movements, and the third for saving the map.
 * gmapping:
```
  roslaunch mailbot_navigation gmapping.launch myWorld:=<example world filename in ROS package> x:=0 y:=0 z:=0 roll:=0 pitch:=0 yaw:=0
```
 * teleop_twist_keyboard
```
  roslaunch mailbot_navigation teleop.launch
```
 * map_server (check the YAML file generated and make sure only the PGM filename is used, such as 'cafe.pgm')
```
  cd ~/src/mailbot_navigation/maps/
  rosrun map_server map_saver -f <myWorld name used for gmapping>
```
- Navigation
Be sure to run the navigation after a gmapping of 
 * :
```
  roslaunch mailbot_navigation gmapping.launch
```
- Spawning
 * To spawn the mailbot in an empty world, run the below command in a terminal
```
  roslaunch env turtlebot3_env_open_spaces_wsh-edit.launch
```
 * To run the project on dynamic world (with moving humans)  .. [work in progress]

        roslaunch env turtlebot3_env_open_spaces_wwh-edit.launch

2. Run the simulation

* To run the simulation, in another sourced terminal:

        rosrun orca test_sim
	
3. Run Obstacle detector package:
* First run split_scan package, then obstacle tracker:

```
 	roslaunch split_scan split_scan.launch
```
```
	roslaunch obstacle_detector detector.launch
```
