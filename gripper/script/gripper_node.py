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
if __name__ == '__main__':
  pcurrent=60.0
  rcurrent=130.0
  gcurrent=60.0
  def pitch(msg,current):
    global pcurrent
    pcurrent=gc.movePitch(-msg.axes[3], current)
    print "pcurrent %s" % pcurrent
  def roll(msg,current):
    global rcurrent
    rcurrent=gc.moveRoll(-msg.axes[2], current)
    print "rcurrent %s" % rcurrent
  def grab(msg,current):
    global gcurrent
    print "msg5 %s" % msg.buttons[5]
    print "msg4 %s" % msg.buttons[4]
    grab=msg.buttons[5]-msg.buttons[4]
    gcurrent=gc.grab(grab, current)
  def callback (msg):
    pitch(msg,pcurrent)
    roll(msg,rcurrent)
    grab(msg,gcurrent)
  try:
    #Initialize node
    rospy.init_node('gripper_node')
    #Create subscriber, and tell it to call js_call() whenever a message is received
    rospy.Subscriber('/joy', Joy, callback)
    #rospy.Subscriber('/joy', Joy, grab)
    #We need to wait for new messages
    rospy.spin()
  #If we are interrupted, catch the exception, but do nothing
  except rospy.ROSInterruptException:
    pass
