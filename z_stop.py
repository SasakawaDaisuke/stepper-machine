# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO


# GPIOの各ピンを指定するため
GPIO.setmode(GPIO.BCM)

ENable_z = 15  # 03pin
CW = 3 #05pin# 1=CW,0=CCW               
CLK = 18 #12pin

# ピンのセットアップ
GPIO.setup(ENable_z, GPIO.OUT)
GPIO.setup(CLK, GPIO.OUT)
GPIO.output(ENable_z, 1)
GPIO.cleanup()