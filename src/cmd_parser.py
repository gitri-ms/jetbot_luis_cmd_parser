#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from ros_msft_luis_msgs.msg import TopIntent

g_pub = rospy.Publisher("cmd_str", String, queue_size=1)

def callback(data):
    intent_str = data.topIntent
    #ROS_INFO("intent_str: %s", intent_str)
    confidence = data.score
    if confidence > 0.5:
        #ROS_INFO("Publishing intent...")
        g_pub.publish(intent_str)

def cmd_parser():
    rospy.init_node('cmd_parser')
    rospy.Subscriber("intent", TopIntent, callback)
    rospy.spin()


if __name__ == '__main__':
    try:
        cmd_parser()
    except rospy.ROSInterruptException:
        pass