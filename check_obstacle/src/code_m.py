#! /usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
def callback(msg):
  j=0
  
  for i in range(0,541):#taking valuse from 0 to 540 from ranges array
     n = []*len(msg.ranges)
     if(msg.ranges[i] < 0.5):#restricting area to different area
        
        print(msg.ranges[i])
        
        n[j]=msg.ranges[i]#coping the obstacle values to new array
        j=j+1
  mi = n[0]#taking mi = n[0] as midpoint of the object
   
  for j in range(0,len(n)):#finding midpoint of the new array
      if(n[j] < mi):
        mi = n[j]
  rospy.loginfo("Center point is: %f", mi)
  rospy.loginfo("First co_ordinate is: %f", n[0])
  rospy.loginfo("Last co_ordinate is: %f", n[len(n)])
  
  pub.publish(move)
  
  
rospy.init_node('check_obstacle')
sub = rospy.Subscriber('/scan', LaserScan, callback)
pub = rospy.Publisher('/cmd_vel', Twist)
move = Twist()

rospy.spin()
