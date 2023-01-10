import RPi.GPIO as GPIO
import time
import sys 

# GPIO 35番を使用
PIN = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
servo = GPIO.PWM(PIN, 50)


servo.start(50)
servo.ChangeDutyCycle(3)
time.sleep(3.0)
servo.ChangeDutyCycle(12)
time.sleep(3.0)
servo.stop()
GPIO.cleanup()
