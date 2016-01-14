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
rcurrent=0
PWM.start("P9_14",0,50)
PWM.start("P9_16",0,50)
PWM.start("P8_13",0,50)
def pitch(msg):
  tamp=gc.movePitch(msg.axes[3], pcurrent)
  global pcurrent
  pcurrent = tamp
  print pcurrent
def roll(msg):
  tamp=gc.moveRoll(msg.axes[2], rcurrent)
  global rcurrent
  rcurrent = tamp
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
