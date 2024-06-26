#!/usr/bin/env python2
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import numpy as np

class Explorer:
    def __init__(self):
        self.sub_scan = rospy.Subscriber('scan', LaserScan, self.callback)
        self.pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        self.velocity_msg = Twist()
        self.distToObstacle = 1

    def callback(self, msg):
        ahead = len(msg.ranges) // 2
        rospy.loginfo(rospy.get_caller_id() + " Distance to obstacle: %s", msg.ranges[ahead])
        if msg.ranges[ahead] > self.distToObstacle:
            # Move forward
            self.velocity_msg.linear.x = 0.25
            self.velocity_msg.angular.z = 0.5
        else:
            # Left or right
            speed = msg.ranges[ahead] / (self.distToObstacle * 2.0)
            room_explore_right = (np.array(msg.ranges[0:ahead]) < (self.distToObstacle)).sum()
            room_explore_left = (np.array(msg.ranges[ahead+1:]) < (self.distToObstacle)).sum()
            if room_explore_left > room_explore_right:
                self.velocity_msg.angular.z = room_explore_right / len(msg.ranges)
            else:
                self.velocity_msg.angular.z = -(room_explore_left / len(msg.ranges))
            self.velocity_msg.linear.x = speed
            # direction = "right"
            # if self.velocity_msg.angular.z > 0.0:
                # direction = "left"
            rospy.loginfo(rospy.get_caller_id() + " Speed: %s", str(self.velocity_msg.angular.z))
        self.pub.publish(self.velocity_msg)

if __name__  == '__main__':
    rospy.init_node('scan_values')
    Explorer()
    rospy.spin()
