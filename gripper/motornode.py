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
#Function which is called every time a JointState is received, if the Subscriber is set up to use this function
GPIO.setup("P9_14", GPIO.OUT) #motor a
GPIO.setup("P9_12", GPIO.OUT)
GPIO.setup("P9_11", GPIO.OUT)
GPIO.setup("P9_16", GPIO.OUT) #motor b
GPIO.setup("P9_15", GPIO.OUT)
GPIO.setup("P9_13", GPIO.OUT)
GPIO.setup("P8_14", GPIO.OUT) #motor c
GPIO.setup("P8_16", GPIO.OUT)
GPIO.setup("P8_13", GPIO.OUT)
PWM.start("P9_14", 0)
PWM.start("P9_16", 0)
PWM.start("P8_13", 0)
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
