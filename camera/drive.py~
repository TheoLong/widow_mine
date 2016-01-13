#!/usr/bin/python
# 4 motor drive depend on velocity, when pwm is + robot move forward
# Author: Yunfei Guo <yunfei96@vt.edu>
import Adafruit_BBIO.GPIO as GPIO
# import adafruit gpio
import Adafruit_BBIO.PWM as PWM
# import adafruit pwm
# control function
def turn(percent):
    power = 0.0
    power=percent*7.9
    round (power,0)
    power=int(power)
    print power
    if power>0: #backward
	power = abs(power)
        GPIO.output("P9_12", GPIO.HIGH)
        GPIO.output("P9_11", GPIO.LOW)
        PWM.set_duty_cycle("P9_14", power)
        GPIO.output("P9_15", GPIO.HIGH)
        GPIO.output("P9_13", GPIO.LOW)
        PWM.set_duty_cycle("P9_16", power)
    if power<0: #forward
	power=abs(power)
        GPIO.output("P9_11", GPIO.HIGH)
        GPIO.output("P9_12", GPIO.LOW)
        PWM.set_duty_cycle("P9_14", power)
        GPIO.output("P9_13", GPIO.HIGH)
        GPIO.output("P9_15", GPIO.LOW)
        PWM.set_duty_cycle("P9_16", power)
    if power == 0: #stop
        power=abs(power)
        GPIO.output("P9_12", GPIO.HIGH)
        GPIO.output("P9_11", GPIO.LOW)
        PWM.set_duty_cycle("P9_14", 0)
        GPIO.output("P9_15", GPIO.HIGH)
        GPIO.output("P9_13", GPIO.LOW)
        PWM.set_duty_cycle("P9_16", 0)
def forward(percent):
    powerf = 0.0
    powerf=percent*7.9
    round (powerf,0)
    powerf=int(powerf)
    if powerf>0: #backward
        powerf=abs(powerf)
        GPIO.output("P8_16", GPIO.HIGH)
        GPIO.output("P8_14", GPIO.LOW)
        PWM.set_duty_cycle("P8_13", powerf)
        GPIO.output("P8_10", GPIO.HIGH)
        GPIO.output("P8_11", GPIO.LOW)
        PWM.set_duty_cycle("P8_19", powerf)
    if powerf<0:
	powerr=abs(powerf)
	GPIO.output("P8_14", GPIO.HIGH)
        GPIO.output("P8_16", GPIO.LOW)
        PWM.set_duty_cycle("P8_13", powerf)
        GPIO.output("P8_11", GPIO.HIGH)
        GPIO.output("P8_10", GPIO.LOW)
        PWM.set_duty_cycle("P8_19", powerf)
    if powerr == 0:
        GPIO.output("P8_14", GPIO.HIGH)
        GPIO.output("P8_16", GPIO.LOW)
        PWM.set_duty_cycle("P8_13", 0)
        GPIO.output("P8_11", GPIO.HIGH)
        GPIO.output("P8_10", GPIO.LOW)
        PWM.set_duty_cycle("P8_19", 0)
def craw(percent):
    powerc = 0.0
    powerc=percent*7.9
    round (powerc,0)
    powerc=int(powerc)
    if powerc>0: #backward
        powerc=abs(powerc)
        GPIO.output("P8_16", GPIO.HIGH)
        GPIO.output("P8_14", GPIO.LOW)
        PWM.set_duty_cycle("P8_13", powerc)
        GPIO.output("P8_10", GPIO.HIGH)
        GPIO.output("P8_11", GPIO.LOW)
        PWM.set_duty_cycle("P8_19", powerc)
    if powerc<0:
	powerr=abs(powerc)
	GPIO.output("P8_14", GPIO.HIGH)
        GPIO.output("P8_16", GPIO.LOW)
        PWM.set_duty_cycle("P8_13", powerc)
        GPIO.output("P8_11", GPIO.HIGH)
        GPIO.output("P8_10", GPIO.LOW)
        PWM.set_duty_cycle("P8_19", powerc)
    if powerc == 0:
        GPIO.output("P8_14", GPIO.HIGH)
        GPIO.output("P8_16", GPIO.LOW)
        PWM.set_duty_cycle("P8_13", 0)
        GPIO.output("P8_11", GPIO.HIGH)
        GPIO.output("P8_10", GPIO.LOW)
        PWM.set_duty_cycle("P8_19", 0)

