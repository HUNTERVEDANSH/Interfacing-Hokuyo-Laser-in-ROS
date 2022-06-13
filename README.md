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
1. Start ROS first
```
   roscore
```
2. Run the rosrun command to let node stream data 
```
   rosrun urg_node urg_node
```
3. Try using the following command to set the default port for the node if port is not set
```
   rosparam set urg_node/port /dev/ttyACM0
```

