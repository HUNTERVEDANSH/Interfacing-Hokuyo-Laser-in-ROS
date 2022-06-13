# Interfacing-Hokuyo-Laser-in-ROS
This repository contains steps to interface Hokuyo [UTM-30LX](https://hokuyo-usa.com/products/lidar-obstacle-detection/utm-30lx) with ROS Noetic.
## Prerequisite
Install and configure ROS Noetic on Ubuntu 20.04 from [here](http://wiki.ros.org/noetic/Installation/Ubuntu)
## Working with Hokuyo Node
Plug in your Hokuyo UTM-30LX to the USB port.<br />
### Steps to be followed
1. Check the permission of the node connected with the command.<br />
```
   ls -l /dev/ttyACM0<br />
```

