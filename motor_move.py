import RPi.GPIO as GPIO
import time

LAPin = 16

GPIO.setmode(GPIO.BOARD) # Use GPIO.BOARD if using Board pin numbers, use GPIO.BCM if using
                         # Broadcom pin designations
GPIO.setup(LAPin, GPIO.OUT)
GPIO.output(LAPin,GPIO.LOW)
pwm = GPIO.PWM(LAPin, 50) # Set pin 16 to be pulse width modulated at a frequency of 50 Hz
pwm.start(4.6)

def move_motor_out():
    print("Moving Motor Out")
    pwm.ChangeDutyCycle(4.7)
    time.sleep(5)
    

def move_motor_in():
    print("Moving Motor in")
    pwm.ChangeDutyCycle(9.2)
    time.sleep(5)
    
    


move_motor_out()

move_motor_in()

##while True:
##    direc = input("Where do you want to move, in = 1, out = 0")
##    print("Output was: ",direc)
##    if direc == 0:
##        print("Move Out")
##        move_motor_out()
##    elif direc == 1:
##        print("Move In")
##        move_motor_in()
##    else:
##        print("No Motion")
##        time.sleep(5)



# try:
# # Just some quick comments. The Actuonix Linear Actuator L16-50-53-6-R will
# # move 2 cm between a retracted position (specified by pwm.ChangeDutyCycle(4.4)) to
# # an extended position (specified by pwm.ChangeDutyCycle(6.7)).
# # This Linear Actuator is completely retracted at pwm.ChangeDutyCycle(4.4),
# # and is fully extended near pwm.ChangeDutyCycle(10.0), although the upper
# # limit has been found to be inconsistent. The Actuator intermittently received
# # values as high as 13.4, and intermittently failed to receive values as low
# # as 9.8.
#     pwm.ChangeDutyCycle(4.4)
#     print("Low")
#     time.sleep(3)
#     pwm.ChangeDutyCycle(6.6)
#     print("Low-Med")
#     time.sleep(3)
#     pwm.ChangeDutyCycle(6.7)
#     print("Med")
#     time.sleep(3)
#     pwm.ChangeDutyCycle(6.8)
#     print("Med-High")
#     time.sleep(3)
#     pwm.ChangeDutyCycle(4.4)
#     print("Low")
#     time.sleep(3)
#
# except KeyboardInterrupt:
#     pwm.stop()
#     GPIO.cleanup()
GPIO.cleanup()
