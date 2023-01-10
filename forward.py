# #!/usr/bin/python
# import time
# import RPi.GPIO as GPIO
# 
# ENable    =  2 #03pin
# CW = 3 #5pin# 1=CW,0=CCW
# CLK     = 18 #12pin
# 
# #init
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(ENable , GPIO.OUT)
# GPIO.output(ENable , 1)
# GPIO.setup(CW , GPIO.OUT)
# GPIO.setup(CLK , GPIO.OUT)
# pwm = GPIO.PWM(CLK, 100) #100Hz Max 200kHz
# pwm.start(50) #duty 50%
# 
# def forward(speed):
#     pwm.start(50)
#     GPIO.output(CW , 1)
#     GPIO.output(ENable , 0)
#     pwm.ChangeFrequency(speed/3)
#     time.sleep(0.1)
#     pwm.ChangeFrequency(speed)
# 
# forward(1000) #1000 is 1kHz

#!/usr/bin/python
import time
import RPi.GPIO as GPIO

ENable    =  2 #03pin
CW = 3 #5pin# 1=CW,0=CCW
CLK     = 18 #12pin

#init
GPIO.setmode(GPIO.BCM)
GPIO.setup(ENable , GPIO.OUT)
GPIO.output(ENable , 1)
GPIO.setup(CW , GPIO.OUT)
GPIO.setup(CLK , GPIO.OUT)
pwm = GPIO.PWM(CLK, 100) #100Hz Max 200kHz
pwm.start(50) #duty 50%

def forward(speed):
    pwm.start(50)
    GPIO.output(CW , 1)
    GPIO.output(ENable , 0)
    pwm.ChangeFrequency(speed/3)
    time.sleep(0.1)
    pwm.ChangeFrequency(speed)


def backwards(speed):
    pwm.start(50)
    GPIO.output(CW, 0)
    GPIO.output(ENable , 0)
    pwm.ChangeFrequency(speed/3)
    time.sleep(0.1)
    pwm.ChangeFrequency(speed)

def Stop():
    GPIO.output(ENable , 0)
    pwm.ChangeDutyCycle(0)
    # pwm.stop()

forward(1000)
time.sleep(10)
# #main
# try:
#     print ("start")
#     forward(1000) #1000 is 1kHz

    
# except:
#     print ("Done!")
#     Stop()
#     GPIO.cleanup()