#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class WallFollower:
   
    def __init__(self):
            global move
            move = Twist()
            self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10) #publish message
            self.sub = rospy.Subscriber("/scan", LaserScan, self.callback) #subscribe message 
            self.ld = 0
            self.rd = 0
            self.amax = 0
            self.amin = 270
            self.count = 0
    def callback(self, msg):
            self.amin = 270 # angle at right side of object
            self.amax = 0 # angle at left side of object
            self.ld = 0
            self.rd = 0
            self.count = 0  
            if (msg.ranges[540] < 9):
    
              if (msg.ranges[540] > 5):
                          move.linear.x = 50
                          move.angular.z = 0.0 
                          rospy.loginfo('Object Distance: %f    Linear Velocity: %d',msg.ranges[540], move.linear.x)
                                             
              if (msg.ranges[540] <= 5) and (msg.ranges[540] > 2.5):
                          move.linear.x = 40 
                          move.angular.z = 0.0 
                          rospy.loginfo('Object Distance: %f    Linear Velocity: %d',msg.ranges[540], move.linear.x)
                          
              if (msg.ranges[540] <= 2.5) and (msg.ranges[540] > 1):
                          move.linear.x = 35
                          move.angular.z = 0.0 
                          rospy.loginfo('Object Distance: %f    Linear Velocity: %d',msg.ranges[540], move.linear.x)
                          
              if (msg.ranges[540] <= 1) and (msg.ranges[540] > 0.5):
                        move.linear.x = 20
                        for i in range(360,700): # for loop to read the data of 540 data points    
                           if (msg.ranges[i] < 1) and (msg.ranges[i] > 0.5):
                             self.count = self.count + 1 # extracting data points less than the desired diatance
                             #print('Angle = ', i*0.25) # calculating angle at each point
                             #print('Distance = ', msg.ranges[i])
            
                             if(i*0.25 > self.amax): # calculating leftmost angle
                               self.amax = i*0.25
                               self.ld = msg.ranges[i] # leftmost distance
                  
                             if(i*0.25 < self.amin): #calculating rightmost angle
                               self.amin = i*0.25 
                               self.rd = msg.ranges[i] # rightmost distance
 
                       if(self.ld > self.rd):
                               move.linear.x = 20
                               move.angular.z = 5
                               print('\nTURNING LEFT\n')
                               rospy.loginfo('\nLeft Distance: %f     Right Distance: %f\n', self.ld, self.rd)
                               rospy.loginfo('\nObject Distance: %f    Angle Max: %f    Linear Velocity: %d     Angular Velocity: %d\n',msg.ranges[540], self.amax, move.linear.x, move.angular.z)
                                                                     
                       if(self.ld < self.rd):                  
                               move.linear.x = 20                    
                               move.angular.z = -5 
                               print('\nTURNING RIGHT\n')
                               rospy.loginfo('\nLeft Distance: %f     Right Distance: %f\n', self.ld, self.rd)                  
                               rospy.loginfo('\nObject Distance: %f    Angle Min: %f    Linear Velocity: %d     Angular Velocity: %d\n',msg.ranges[540], self.amin, move.linear.x, move.angular.z)
                      
              
                   
              if (msg.ranges[540] < 0.5): 
                          move.linear.x = 0.0
                          move.angular.z = 0.0
                          rospy.loginfo('Object Distance: %f    Linear Velocity: %d',msg.ranges[540], move.linear.x)
                                            
                          
                          
              
            self.pub.publish(move)
                   
                   
if __name__ == "__main__":
    rospy.init_node('check_obstacle')
    WallFollower()
    rospy.spin()



