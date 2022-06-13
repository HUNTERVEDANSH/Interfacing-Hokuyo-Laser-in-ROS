#!/usr/bin/env python
import rospy # Python library for ROS
from sensor_msgs.msg import LaserScan #import library for lidar sensor
from geometry_msgs.msg import Twist #import geometry form twist 
class Circling(): #main class
   
    def __init__(self): #main function
        global circle
        circle = Twist() #create object of twist type  
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10) #publish message
        self.sub = rospy.Subscriber("/scan", LaserScan, self.callback) #subscribe message 
        #self.j=0
        #self.data = [None]*100

    def callback(self, msg): #function for obstacle avoidance
        print('-------RECEIVING LIDAR SENSOR DATA-------')
        for i in range(0,810):
           if(msg.ranges[i] < 0.5):
             #data[self.j] =  
             print(i*0.25)
             print(msg.ranges[i])
             self.data[self.j] = msg.ranges[i]
             self.j = self.j + 1
        for self.j in range(0,len(self.data)):
             self.range_center = self.data[int(len(self.data)/2)]
             self.range_left = self.data[len(self.data)-1]
             self.range_right = self.data[0]
             print(self.range_center)
             print(self.range_left)
             print(self.range_right) 
             
        #print(max(msg.ranges[i]))
        #print('Front: {}'.format(msg.ranges[540])) #lidar data for front side
        #print('Back Right:  {}'.format(msg.ranges[0])) #lidar data for left side
        #print('Back Left: {}'.format(msg.ranges[1080])) #lidar data for right side
        #print('Back: {}'.format(msg.ranges[])) #lidar data for back side
      
      	#Obstacle Avoidance
        #self.distance = 0.7
        #if msg.ranges[0] > self.distance and msg.ranges[270] > self.distance and msg.ranges[540] > self.distance and msg.ranges[810] > self.distance and msg.ranges[1080] > self.distance: 
        #when no any obstacle near detected
            #circle.linear.x = 0.5 # go (linear velocity)
            #circle.angular.z = 0.1 # rotate (angular velocity)
            #rospy.loginfo("Circling") #state situation constantly
        #else: #when an obstacle near detected
            #rospy.loginfo("An Obstacle Near Detected") #state case of detection
            #circle.linear.x = 0.0 # stop
            #circle.angular.z = 0.5 # rotate counter-clockwise
            #if msg.ranges[0] > self.distance and msg.ranges[270] > self.distance and msg.ranges[540] > self.distance and msg.ranges[810] > self.distance and msg.ranges[1080] > self.distance:
                #when no any obstacle near detected after rotation
                #circle.linear.x = 0.5 #go
                #circle.angular.z = 0.1 #rotate
        #self.pub.publish(circle) # publish the move object

if __name__ == '__main__':
    rospy.init_node('check_obstacle') #initilize node
    Circling() #run class
    rospy.spin() #loop it
