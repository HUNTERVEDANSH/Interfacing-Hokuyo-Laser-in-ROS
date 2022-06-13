#!/usr/bin/env python3
import rospy # Python library for ROS
from sensor_msgs.msg import LaserScan # LaserScan type message is defined in sensor_msgs
from geometry_msgs.msg import Twist # geometry message for turn

def callback(msg):
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)  
                            				
    sub = rospy.sub = rospy.Subscriber("/scan", LaserScan, callback)  

    if (msg.ranges[540] > 5):
        move.linear.x = 30 # go forward (linear velocity)
        move.angular.z = 0.0 
        print(msg.ranges[540])
    if (msg.ranges[540] < 5) and (msg.ranges[540] > 2.5):                                                                  
        move.linear.x = 20 
        move.angular.z = 0.0 
        print(msg.ranges[540])
    if (msg.ranges[540] <= 2.5) and (msg.ranges[540] > 1:
        move.linear.x = 10 
        move.angular.z = 0.0 
        print(msg.ranges[540])
    if (msg.ranges[540] <= 1) and (msg.ranges[540] > 0.5:
        move.linear.x = 5
        move.angular.z = 0.0
        print(msg.ranges[540])
    if msg.ranges[540] < 0.5:
        move.linear.x = 0.0
        move.angular.z = 0.0
        print(msg.ranges[540])
        
        
        
    pub.publish(move) # publish the move object


move = Twist() # Creates a Twist message type object
 
if __name__ == '__main__':
    rospy.init_node('check_obstacle')
    rospy.spin() 
