#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
def callback(msg):
  if msg.ranges[540]>0.5
     move.linear.x = 0.5
     move.angular.z = 0.0
     print(msg.ranges[540])
  print "Number of Readings: ", print len(msg.ranges)
  print "Reading at position:", msg.ranges[540]   
  if msg.ranges[540]<0.5
     move.linear.x = 0.0
     move.angular.z = 0.0
     print(msg.ranges[540]) 
  pub.publish(move)
  
  
rospy.init_node('check_obstacle')
sub = rospy.Subscriber('/scan', LaserScan, callback)
pub = rospy.Publisher('/cmd_vel', Twist)
move = Twist()

rospy.spin()
