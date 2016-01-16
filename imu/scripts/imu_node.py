#!/usr/bin/python
import rospy
import time
from sensor_msgs.msg import Imu
from imu_class import imu
def update_imu(arg):
  imu_msg = Imu()
  imu_msg.header.frame_id = "imu_msg"
  imu_msg.header.stamp  = arg.current_real
  imu_msg.header.orientation : {
    x : imu.readMAGx(),
    y : imu.readMAGy(),
    z : imu.readMAGz()
    }
  imu_msg.orientation_covariance : [0,0,0,0,0,0,0,0,0]
  imu_msg.angular_velocity : {
    x : imu.readGYRx(),
    y : imu.readGYRy(),
    z : imu.readGYRz()
    }
  imu_msg.angular_velocity_covariance  : [0,0,0,0,0,0,0,0,0],
  imu_msg.linear_acceleration : {
     x : imu.readACCx(),
     y : imu.readACCy(),
     z : imu.readACCz()
     }
  imu_msg.linear_acceleration_covariance  : [0,0,0,0,0,0,0,0,0]
  rospy.loginfo(imu_msg)
  pub.publish(imu_msg)
if __name__ == '__main__':
  try:
    rospy.init_node('imu_node')
    pub = rospy.Publisher('/imu_msg', Imu, queue_size=10)
    timer = rospy.Timer(rospy.Duration(0.0000001), update_imu)
    rospy.spin()
  except rospy.ROSInterruptException:
    pass
