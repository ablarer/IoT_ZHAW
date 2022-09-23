#!/usr/bin/env python3

'''
                    ___           ___           ___
        ___        /\__\         /\  \         /\  \
       /\  \      /::|  |       /::\  \       /::\  \
       \:\  \    /:|:|  |      /:/\:\  \     /:/\ \  \
       /::\__\  /:/|:|  |__   /::\~\:\  \   _\:\~\ \  \
    __/:/\/__/ /:/ |:| /\__\ /:/\:\ \:\__\ /\ \:\ \ \__\
   /\/:/  /    \/__|:|/:/  / \:\~\:\ \/__/ \:\ \:\ \/__/
   \::/__/         |:/:/  /   \:\ \:\__\    \:\ \:\__\
    \:\__\         |::/  /     \:\ \/__/     \:\/:/  /
     \/__/         /:/  /       \:\__\        \::/  /
                   \/__/         \/__/         \/__/


    File:          toggle.py


    Purpose:       Trivial implementation
                   of a LED toggler on a
                   Raspberry Pi and a 
                   GrovePi board attached.


    Remarks:       - The grovepi module and all
                     its dependencies have to be
                     available on the system
                     this script has to be run.

                   - 2 LEDs connected to the
                     GrovePi board (pins see 
                     in globals section).

                   - 1 rotary angle sensor
                     connected to the GrovePi
                     board (pins see in 
                     globals section).

                   - Use the rotary angle sensor
                     (potentiometer) to adjust
                     the toggling interval of
                     the two LEDs.


    Author:        Your Name <--------@students.zhaw.ch>


    Date:          09/2016

'''

import time

import grovepipip

LED0_PIN = int(3)
LED1_PIN = int(4)

ROTARY_ANGLE_SENSOR_PIN = int(0)
ROTARY_ANGLE_SENSOR_RES = int(1024)

'''
maximum sleep time [ms] would be:
SLEEP_TIME_RESOLUTION * SLEEP_TIME_STEP_IN_MILLIS
'''
SLEEP_TIME_RESOLUTION = int(12)
SLEEP_TIME_STEP_IN_MILLIS = int(200)

# globals section
#define GROVE_VCC 5    //VCC of the grove interface is normally 5v
#define FULL_ANGLE 300 //full value of the rotary angle is 300 degrees
GROVE_VCC = 5
FULL_ANGLE = 300
current_state = int(0)

rotary_angle_sensor_raw = int(0)

grovepi.pinMode(ROTARY_ANGLE_SENSOR_PIN, "INPUT")
grovepi.pinMode(LED0_PIN, "OUTPUT")
grovepi.pinMode(LED1_PIN, "OUTPUT")
time.sleep(float(1.0))


def read_rotary_angle_sensor():
    global rotary_angle_sensor_raw
    sleep_time = int(0)

    try:
        # ... read sensor here
        # Read sensor value
        rotary_angle_sensor_raw = grovepi.analogRead(ROTARY_ANGLE_SENSOR_PIN)

        # Calculate PH
        voltage = rotary_angle_sensor_raw * GROVE_VCC / 1023
        degrees = (voltage * FULL_ANGLE) / GROVE_VCC
        angle_divison  = int(degrees / 12) # e.g. 300 / 12 = 25

        if degrees <=  1 * angle_divison:
          sleep = 200
        elif degrees <= 2 * angle_divison:
          sleep = 400
        elif degrees <= 3 * angle_divison:
          sleep = 600
        elif degrees <= 4 * angle_divison:
          sleep = 800
        elif degrees <= 5 * angle_divison:
          sleep = 1000
        elif degrees <= 6 * angle_divison:
          sleep = 1200
        elif degrees <= 7 * angle_divison:
          sleep = 1400
        elif degrees <= 8 * angle_divison:
          sleep = 1600
        elif degrees <= 9 * angle_divison:
          sleep = 1800
        elif degrees <= 10 * angle_divison:
          sleep = 2000
        elif degrees <= 11 * angle_divison:
          sleep = 2200
        else:
          sleep = 2400
        pass

    except IOError:
        print("Error reading rotary angle sensor.")

    return sleep_time


def toggle_leds():
    # toggle the state of your leds here
    # and write the state to the digital pins
    global current_state

    current_state = grovepi.input(LED0_PIN)
    if current_state:
        grovepi.digitalWrite(LED0_PIN, int(0))
    else:
        grovepi.digitalWrite(LED0_PIN, int(1))

    current_state = grovepi.input(LED1_PIN)
    if current_state:
        grovepi.digitalWrite(LED1_PIN, int(0))
    else:
        grovepi.digitalWrite(LED1_PIN, int(1))
    pass


def main():
    while True:

        try:
            # read_rotary_angle_sensor()
            read_rotary_angle_sensor()
            # This is the time delay of the minimum toggling interval
            time.sleep(0.2)
            sleep_time(sleep)
            # toggle the leds if time is up
            toggle_leds()


        except KeyboardInterrupt:
            # set all output pins to low.
            grovepi.digitalWrite(LED0_PIN, int(0))
            grovepi.digitalWrite(LED1_PIN, int(0))
            print("program was interrupted by key stroke. exiting ...")
            break


if __name__ == "__main__":
    main()
