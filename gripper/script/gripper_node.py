#!/usr/bin/python
# this node receive msg form rqt stuff and give command based on velocity.
# Author: Yunfei Guo <yunfei96@vt.edu>

# Import the Default ROS tools
import rospy
# Import the JointState message from sensor_msgs
from sensor_msgs.msg import Joy
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import gripper_control as gc
pcurrent=0
rccrent=0
def pitch(msg):
  global pcurrent
  pcurrent=gc.movePitch(msg.axes[3], pcurrent)
def roll(msg):
  global rcurrent
  rcurrent=gc.moveRoll(msg.axes[2], rcurrent)
#def grab(msg):
  #gc.grab(msg.axes[3], gcurrent)
if __name__ == '__main__':
  try:
    #Initialize node
    rospy.init_node('motornode')
    #Create subscriber, and tell it to call js_call() whenever a message is received
    rospy.Subscriber('/joy', Joy, pitch)
    rospy.Subscriber('/joy', Joy, roll)
    #rospy.Subscriber('/joy', Joy, grab)
    #We need to wait for new messages
    rospy.spin()
  #If we are interrupted, catch the exception, but do nothing
  except rospy.ROSInterruptException:
    pass
