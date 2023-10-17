#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from neopixel import *
import argparse
import os
import subprocess
# LED strip configuration:
LED_COUNT      = 64      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


def kill():
    try:
            print("Killing otherz")
#            os.system("ps -aux | grep '.py' | grep -v 'grep\|led-off.py'")
            os.system("d=$(pgrep -f led-off.py| xargs); pgrep -f py | xargs kill -9")
            print("Done killing")
    except:
           print("Process not found")
wait = 50
# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        time.sleep(wait_ms/1000.0)
        strip.setPixelColor(i, color)
        strip.show()

def default_off(strip, wait):
    print("first color")
    colorWipe(strip, Color(0,255,0), wait)
    colorWipe(strip, Color(0,0,255), wait)
    colorWipe(strip, Color(255,0,0), wait)
    colorWipe(strip, Color(0,0,0), wait)
    colorWipe(strip, Color(0,0,0), wait)
    colorWipe(strip, Color(0,0,0), wait)
    colorWipe(strip, Color(0,0,0), wait)
    print("Off")
    kill()
def hot_off(strip, wait):
    colorWipe(strip, Color(150,255,0), wait)
    colorWipe(strip, Color(125,255,0), wait)
    colorWipe(strip, Color(100,255,0), wait)
    colorWipe(strip, Color(75,255,0), wait)
    colorWipe(strip, Color(50,255,0), wait)
    colorWipe(strip, Color(25,255,0), wait)
    colorWipe(strip, Color(0,0,0), wait)
    colorWipe(strip, Color(0,0,0), wait)
    colorWipe(strip, Color(0,0,0), wait)
    colorWipe(strip, Color(0,0,0), wait)
    error_off(strip, wait)
    colorWipe(strip, Color(0,0,0), wait)
    colorWipe(strip, Color(0,0,0), wait)
    colorWipe(strip, Color(0,0,0), wait)
    colorWipe(strip, Color(0,0,0), wait)

    kill()
def error_off(strip, wait):
    colorWipe(strip, Color(0,255,0), wait)
    colorWipe(strip, Color(0,0,0), wait)
    colorWipe(strip, Color(0,255,0), wait)
    colorWipe(strip, Color(0,0,0), wait)
    colorWipe(strip, Color(0,255,0), wait)
    colorWipe(strip, Color(0,0,0), wait)
    kill()

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    parser.add_argument('-t', '--hot', action='store_true', help='Temp to hot warning')
    parser.add_argument('-e', '--error', action='store_true', help='Error')
    parser.add_argument('-f', '--off', action='store_true', help='off')
    args = parser.parse_args()

    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    # Create NeoPixel object with appropriate configuration.
    if args.hot:
        hot_off(strip, 50)
        default_off(strip, 50)
    elif args.error:
        error_off(strip, 50)
    elif args.off:
        colorWipe(strip, Color(0,0,0), wait)
        colorWipe(strip, Color(0,0,0), wait)
        colorWipe(strip, Color(0,0,0), wait)
        colorWipe(strip, Color(0,0,0), wait)
        colorWipe(strip, Color(0,0,0), wait)
    else:
        print("Default opt")
        default_off(strip, 50)
    kill()

#    colorWipe(strip, Color(0,0,0), 5)

