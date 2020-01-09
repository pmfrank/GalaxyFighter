#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

fire = False

RoAPin = 11
RoBPin = 12
BtnPin = 13
GPIO.setwarnings(False)
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(RoAPin, GPIO.IN)
    GPIO.setup(RoBPin, GPIO.IN)
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

class Control():

    def __init__(self):
        self.flag = 0

    def instruction(self,BtnPin):
        
        current_rob_status = None
        last_rob_status = 0

        last_rob_status = GPIO.input(RoBPin)
        while(not GPIO.input(RoAPin)):
            current_rob_status = GPIO.input(RoBPin)
            self.flag = 1
        if self.flag == 1:
            flag = 0
            if (last_rob_status == 0) and (current_rob_status == 1):
                return 'LEFT'
            if (last_rob_status == 1) and (current_rob_status == 0):
                return 'RIGHT'

    def btnISR(self, channel):
        global fire
        fire = True


setup()
control = Control()
GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=control.btnISR, bouncetime=100)

while True:
    try:
        move = control.instruction(None)
        if move != None:
            print(move)
        if fire:
            print('FIRE')
            fire = False
    except KeyboardInterrupt:
        GPIO.cleanup()
        break
    except Exception as e:
        GPIO.cleanup()
        print(e)
        break
