# Controlling a Servo Motor using RaspberryPi
# Isaac, April 24, 2019
# UBCO ATFL
# This code makes use of Pin 16 on the RaspberryPi (GPIO4) to send a pulse width
# modulated signal (of varying duty cycle) to the servo motor. The pulse width 
# modulation frequency is set at 50 Hz, but the duty cycle of the modulated signal 
# is varied to command different servo motor positions. For example, a typical servo 
# motor may be at a 0-degree positions when the duty cycle is set to 2.5%, a 90-degree
# position when the duty cycle is set to 7.5%, and a 180-degree position when the 
# duty cycle is set to 12.5%. As seen in the code below, the position of the servo 
# motor is changed using the pwm.ChangeDutyCycle() command, where the desired duty 
# cycle percentage is placed within the empty command brackets. The minimum and maximum 
# values will need to be found for each unique servo motor, and these values can be 
# found by experimenting with the commanded positions.

import RPi.GPIO as GPIO
import time

LAPin = 16

GPIO.setmode(GPIO.BOARD) # Use GPIO.BOARD if using Board pin numbers, use GPIO.BCM if using
                         # Broadcom pin designations
GPIO.setup(LAPin, GPIO.OUT)
GPIO.output(LAPin,GPIO.LOW)
pwm = GPIO.PWM(LAPin, 50) # Set pin 16 to be pulse width modulated at a frequency of 50 Hz
pwm.start(7.5)

try:
# Just some quick comments. The Actuonix Linear Actuator L16-50-53-6-R will
# move 2 cm between a retracted position (specified by pwm.ChangeDutyCycle(4.4)) to
# an extended position (specified by pwm.ChangeDutyCycle(6.7)).
# This Linear Actuator is completely retracted at pwm.ChangeDutyCycle(4.4),
# and is fully extended near pwm.ChangeDutyCycle(10.0), although the upper
# limit has been found to be inconsistent. The Actuator intermittently received
# values as high as 13.4, and intermittently failed to receive values as low
# as 9.8. 
    pwm.ChangeDutyCycle(4.4)
    print("Low")
    time.sleep(3)
    pwm.ChangeDutyCycle(6.6)
    print("Low-Med")
    time.sleep(3)
    pwm.ChangeDutyCycle(6.7)
    print("Med")
    time.sleep(3)
    pwm.ChangeDutyCycle(6.8)
    print("Med-High")
    time.sleep(3)
    pwm.ChangeDutyCycle(4.4)
    print("Low")
    time.sleep(3)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
