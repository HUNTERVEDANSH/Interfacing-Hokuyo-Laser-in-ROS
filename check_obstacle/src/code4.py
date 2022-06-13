#!/usr/bin/env python
import rospy # Python library for ROS
from sensor_msgs.msg import LaserScan #import library for lidar sensor
from geometry_msgs.msg import Twist #import geometry form twist 
class laser_scan_data(): #main class

    def __init__(self): #main function
        global circle
        circle = Twist() #create object of twist type  
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10) #publish message
        self.sub = rospy.Subscriber("/scan", LaserScan, self.callback) #subscribe message 
        
    def callback(self, msg): #function for obstacle avoidance
        print('-------RECEIVING LIDAR SENSOR DATA-------')
        for i in range(0,1079):
           if(msg.ranges[i] < 0.5): 
             print(i*0.25)
             print(msg.ranges[i])
          
if __name__ == '__main__':
    rospy.init_node('check_obstacle') #initilize node
    laser_scan_data() #run class
    rospy.spin() #loop it
