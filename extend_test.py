import RPi.GPIO as GPIO
import time
import numpy

#------------------------Pin definitions------------------------#
# Pin Definitions:
vacuum_pump = 4 # Broadcom pin 17 (P1 pin 11)
linear_actuator_extend = 27 # Broadcom pin 5 (P1 pin 13)
linear_actuator_unlock_retract = 22 # Broadcom pin 12 (P1 pin 15)

#---------------------------------------------------------------------#
# Pin Setup:
GPIO.setmode(GPIO.BCM)    # There are two options for this, but just use the board one for now. Don't worry much about it, we can check the definitions when I get back
GPIO.setup(linear_actuator_extend, GPIO.OUT) # Specifies linear_actuator_extend pin as an output
GPIO.setup(linear_actuator_unlock_retract, GPIO.OUT) # Specifies linear_actuator_unlock_retract pin as an output
GPIO.setup(vacuum_pump, GPIO.OUT) # Specifies vacuum_pump pin as an output

# Initial state for outputs:
GPIO.output(vacuum_pump, GPIO.LOW)

# Initial state for outputs:
GPIO.output(linear_actuator_extend, GPIO.LOW)
GPIO.output(linear_actuator_unlock_retract, GPIO.LOW)

for i in range(1):

    ##
    GPIO.output(linear_actuator_extend, GPIO.HIGH)  # Actuate linear actuator to extended position
    GPIO.output(linear_actuator_unlock_retract, GPIO.LOW)  # Energizing both control wires causes linear actuator to extend

    time.sleep(1)
    ####
    GPIO.output(linear_actuator_extend, GPIO.LOW)  # Actuate linear actuator to extended position
    GPIO.output(linear_actuator_unlock_retract, GPIO.HIGH)  # Energizing both control wires causes linear actuator to extend

    time.sleep(0.5)


GPIO.output(linear_actuator_extend, GPIO.LOW)
GPIO.output(linear_actuator_unlock_retract, GPIO.LOW)

GPIO.cleanup()
