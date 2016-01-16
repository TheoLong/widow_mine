#!/usr/bin/python
# Put the description of your file here
# Author: Your Name <your_email@vt.edu>

# Import the Default ROS tools
import rospy
import time
import Adafruit_BBIO.GPIO as GPIO
# Import the JointState message from sensor_msgs
from sensor_msgs.msg import JointState
from quadrature import QuadratureEstimator
encoderr = QuadratureEstimator()
encoderl = QuadratureEstimator()
GPIO.setup("P9_23", GPIO.IN)
GPIO.setup("P9_24", GPIO.IN)
GPIO.setup("P8_17", GPIO.IN)
GPIO.setup("P8_26", GPIO.IN)
def update_encoders(arg):
#Fix indentation
  encoderr.update(GPIO.input("P9_23"),GPIO.input("P9_24"),rospy.get_rostime().to_sec())
  left = JointState()
#Add joint name and timestamps
  print rospy.get_rostime().to_sec()
  left.header.frame_id = "front_left_wheel_link"
  left.header.stamp  = arg.current_real
  left.position.append(encoderr.position) 
  left.velocity.append(encoderr.velocity)
  encoderl.update(GPIO.input("P8_17"),GPIO.input("P8_26"),rospy.get_rostime().to_sec())
  right = JointState()
  right.header.frame_id = "front_right_wheel_link"
  right.header.stamp = arg.current_real
  right.position.append(encoderl.position) 
  right.velocity.append(encoderl.velocity)
  rospy.loginfo(left)
  publ.publish(left)
  rospy.loginfo(right)
  pubr.publish(right)
  rearleft = JointState()
  rearleft.header.frame_id = "rear_left_wheel_link"
  rearleft.header.stamp = arg.current_real
  rearleft.position.append(encoderr.position)
  rearleft.velocity.append(encoderr.velocity)
  rospy.loginfo(rearleft)
  rearright = JointState()
  rearright.header.frame_id = "rear_right_wheel_link"
  rearright.header.stamp = arg.current_real
  rearright.position.append(encoderl.position)
  rearright.velocity.append(encoderl.velocity)
if __name__ == '__main__':
  try:
    rospy.init_node('encodernode')
    
    #left.velocity = None
    #left.position = None
    
    #right.velocity = None
    #right.position = None
    pubr = rospy.Publisher('/rear_right_wheel/encoder', JointState, queue_size=10)
    publ = rospy.Publisher('/rear_left_wheel/encoder', JointState, queue_size=10)
    pubrr = rospy.Publisher('/front_right_wheel/encoder',JointState, queue_size=10) 
    pubrl = rospy.Publisher('/front_left_wheel/encoder', JointState, queue_size=10)
    #TODO: Verify this syntax

    timer = rospy.Timer(rospy.Duration(0.0000001), update_encoders)
    rospy.spin()
  except rospy.ROSInterruptException:
    pass
