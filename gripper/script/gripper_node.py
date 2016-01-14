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
PWM.start("P9_14",0,50)
PWM.start("P9_16",0,50)
PWM.start("P8_13",0,50)


def pitch(msg,pcurrent):
  print pcurrent
  print msg.axes[3]
  temp=gc.movePitch(msg.axes[3], pcurrent)
  pcurrent = temp
  print temp
def roll(msg,rcurrent):
  print rcurrent
  temp=gc.moveRoll(msg.axes[2], rcurrent)
  rcurrent = temp
#def grab(msg):
  #gc.grab(msg.axes[3], gcurrent)
if __name__ == '__main__':
  tmsg=Joy
  def msg_function(msg):
    tmsg=msg
    print tmsg.axis[3]
  pcurrent=0.0
  rcurrent=0.0
  try:
    #Initialize node
    rospy.init_node('gripper_node')
    #Create subscriber, and tell it to call js_call() whenever a message is received
    rospy.Subscriber('/joy', Joy, msg_function)
    pitch(tmsg,pcurrent)
    roll(tmsg,rcurrent)
    #rospy.Subscriber('/joy', Joy, grab)
    #We need to wait for new messages
    rospy.spin()
  #If we are interrupted, catch the exception, but do nothing
  except rospy.ROSInterruptException:
    pass
