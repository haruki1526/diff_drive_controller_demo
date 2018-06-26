#!/usr/bin/env python
import rospy

from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    rospy.init_node('joy_control')

    def joy_stick(joy_msg):
        twist =Twist()
        twist.linear.x =joy_msg.axes[1] * 1.0
        twist.angular.z = joy_msg.axes[0] * 1.0
        pub.publish(twist)



    sub = rospy.Subscriber('joy', Joy, joy_stick, queue_size=1)
    pub = rospy.Publisher('/robosys/diff_drive_controller/cmd_vel', Twist, queue_size=1)
    
    
    rospy.spin()
