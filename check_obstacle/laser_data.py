#!/usr/bin/env python
import rospy # Python library for ROS
from sensor_msgs.msg import LaserScan #import library for lidar sensor
from geometry_msgs.msg import Twist #import geometry form twist 

def callback(msg):
    print len(msg.ranges)
rospy.init_node('check_obstacle')
sub = rospy.Subcriber('/scan', LaserScan, callback)
rospy.spin()
