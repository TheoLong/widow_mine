#!/usr/bin/python
# 4 motor drive depend on velocity, when pwm is + robot move forward
# Author: Yunfei Guo <yunfei96@vt.edu>
import Adafruit_BBIO.GPIO as GPIO
# import adafruit gpio
import Adafruit_BBIO.PWM as PWM
# import adafruit pwm

class PWM(self):
    def __init__(self):
	self.pwm_row = pwm_row
	self.pwm_pitch = pwm_pitch
	self.pwm_gripper = pwm_gripper
	PWM.start("P9_14",0,50)
	PWM.start("P9_16",0,50)
	PWM.start("P8_13",0,50)
    def row(self, angle):
        pwm_row = 0.0
        pwm_row = angle*0.05333+2.4
	PWM.set_duty_cycle("P9_16", pwm_row)
    def pitch(self, angle):
	pwm_pitch = 0.0
        pwm_pitch = angle*0.05333+2.4
	PWM.set_duty_cycle("P9_16", pwm_pitch)
    def gripper(self, angle):
        pwm_gripper = 0.0
        pwm_gripper = angle*0.05333+2.4
	PWM.set_duty_cycle("P9_16", pwm_gripper)
