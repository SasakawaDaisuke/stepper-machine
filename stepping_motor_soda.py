#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO

ENable = 2 #03pin
CW = 3 #5pin# 1=CW,0=CCW
CLK = 18 #12pin

#init
GPIO.setmode(GPIO.BCM)
GPIO.setup(ENable , GPIO.OUT)
GPIO.output(ENable , 1)
GPIO.setup(CW , GPIO.OUT)
GPIO.setup(CLK , GPIO.OUT)
pwm = GPIO.PWM(CLK, 100) #100Hz Max 200kHz
pwm.start(50) #duty 50%

def forward(speed):
    GPIO.output(CW , 1)
    GPIO.output(ENable , 0)
    print ("forward ",speed)
    pwm.ChangeFrequency(speed/3) #
    time.sleep(0.1)
    pwm.ChangeFrequency(speed)

def backwards(speed):
    GPIO.output(CW, 0)
    GPIO.output(ENable , 0)
    print ("backwards",speed)
    pwm.ChangeFrequency(speed/3)
    time.sleep(0.1)
    pwm.ChangeFrequency(speed)

def Stop():
    GPIO.output(ENable , 0)
    pwm.stop()

#main
"""
try:
    print ("start")
    #while 1:
    s = input('Enter rotaional direction: (FORWARD:a BACKWARD:b)')
    print(s)
    print(type(s))
    forward(1000) #1000 is 1kHz
    time.sleep(5)
    backwards(500)
    time.sleep(5)
    Stop()
    GPIO.cleanup()
except:
    print ("Done!")
    Stop()
    GPIO.cleanup()
"""

print('start!')
s = input('Enter rotational direction (FORWARD:a BACKWARD:b):')
print('{s}')
print(type(s))
GPIO.cleanup()
