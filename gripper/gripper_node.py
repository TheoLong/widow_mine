#!/usr/bin/python
# this node receive msg form rqt stuff and give command based on velocity.
# Author: Yunfei Guo <yunfei96@vt.edu>

# Import the Default ROS tools
import rospy
# Import the JointState message from sensor_msgs
from sensor_msgs.msg import JointState
import drivedemo
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
from drive.py import pwm as pwm
def forward(msg):
  drive.forward(msg.axes[3]*100)
def turn(msg):
  drive.turn(msg.axes[3]*100)
def craw(msg):
  drive.craw(msg.axes[3]*100)
if __name__ == '__main__':
  try:
    #Initialize node
    rospy.init_node('motornode')
    #Create subscriber, and tell it to call js_call() whenever a message is received
    rospy.Subscriber('/joy', Joy, forward)
    rospy.Subscriber('/joy', Joy, turn)
    rospy.Subscriber('/joy', Joy, craw)
    #We need to wait for new messages
    rospy.spin()
  #If we are interrupted, catch the exception, but do nothing
  except rospy.ROSInterruptException:
    pass
