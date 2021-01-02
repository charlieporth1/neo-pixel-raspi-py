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
import sys
import utils as cc
EPSILON = sys.float_info.epsilon  # Smallest possible difference.
# LED strip configuration:
LED_COUNT      = 32      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000   # LED signal frequency in hertz (usually 800khz)  800000 
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
STEPS_DEFA     = 0


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms = 50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
#        time.sleep(wait_ms/1000.0)
        strip.setPixelColor(i, color)
        strip.show()
def revsere():
      for c in reversed(range(0,256)):
                  colorWipe(strip, Color(c,c,c), 1)
                  print("i c ", c)
                  if c >= 253:
                     break

# Main program logic follows:
if __name__ == '__main__':
    wait_ms = 50
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    try:
         while True:
           for i in range(0,256):
             if i >= 253:
                 revsere()
             else:
                  colorWipe(strip, Color(i,i,i), 1)
             print("i ", i)
    except KeyboardInterrupt:
         if args.clear:
            colorWipe(strip, Color(0,0,0), 10)
