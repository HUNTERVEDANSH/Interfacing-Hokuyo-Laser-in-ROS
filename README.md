# Interfacing-Hokuyo-Laser-in-ROS
This repository contains steps to interface Hokuyo [UTM-30LX](https://hokuyo-usa.com/products/lidar-obstacle-detection/utm-30lx) with ROS Noetic.
## Prerequisite
Install and configure ROS Noetic on Ubuntu 20.04 from [here](http://wiki.ros.org/noetic/Installation/Ubuntu)
## Working with Hokuyo Node
**Plug in your Hokuyo UTM-30LX to the USB port**<br />
1. Check the permission of the node connected<br />
```
   ls -l /dev/ttyACM0
```
2. Change permissiom to read and write to all users
```
   sudo chmod a+rw /dev/ttyACM0
```
## Read data from Hokuyo Node
1. Start ROS first using [roscore](http://wiki.ros.org/roscore) command 
```
   roscore
```
2. Run the [rosrun](http://wiki.ros.org/rosbash#rosrun) command to let node stream data 
```
   rosrun urg_node urg_node
```
3. Try using the [rosparam](http://wiki.ros.org/rosparam) command to set the default port for the node if port is not set
```
   rosparam set urg_node/port /dev/ttyACM0
```
4. To check that node is publishing to **/scan** first use [rostopic](http://wiki.ros.org/rostopic#:~:text=rostopic%20contains%20the%20rostopic%20command,and%20interacting%20with%20topics%20dynamically.) command to view all active topic and chech the /scan
```
   rostopic list
```
5. Now check the messages being published to **/scan**
```
   rostopic echo /scan
```
## Visulizing Data 
1. LRF(Hokuyu UTM-30LX) data can be visualized using [RViz](http://wiki.ros.org/rviz) 
```
   rosrun rviz rviz
```
RViz window looks like [this](https://ardupilot.org/dev/docs/ros-rviz.html). 
Click add, then select the topic /scan. If you have an error related to tf, you need to manually enter your fixed frame as “/laser” in the textbox next to fixed frame on the left side of the GUI.

