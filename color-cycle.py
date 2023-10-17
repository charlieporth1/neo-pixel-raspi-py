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
LED_COUNT      = 64      # Number of LED pixels.
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
        time.sleep(wait_ms/1000.0)
        strip.setPixelColor(i, color)
        strip.show()

def define_colors(args):
           colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0)]  # [BLUE, GREEN, RED]
           if args.more:
               colors = [(0, 0, 255), (0, 255, 255),(0, 255, 0), (255, 255, 0), (255, 0, 0), (255, 0, 255)]  # [BLUE, GREEN, RED]

           if args.white:
               colors.append((0, 0, 0))
               colors.append((255, 255, 255))

           return colors

def default_cycle(strip, colors = [], wait_ms = 50):
          for color in colors:
              print("On Color " + str(color))
              r, g, b = color
              colorWipe(strip, Color(r,g,b), wait_ms)

def slow_cycle(strip, args, colors = [], wait_ms = 100):
           minval, maxval = 1,2
           multipler = 1
           if args.win95 or args.slow:
                multipler = 10 if not args.slow else 3
           else:
                multipler = 1
           steps = 10 * multipler if args.steps == STEPS_DEFA else args.steps
           delta = float(maxval-minval) / steps
           print('  Val       R    G    B')
           for i in range(steps+1):
               val = minval + i*delta
               r, g, b = cc.convert_to_rgb(minval, maxval, val, colors)
               print('{:.3f} -> ({:3d}, {:3d}, {:3d})'.format(val, r, g, b))
               colorWipe(strip, Color(r,g,b), wait_ms)

# Main program logic follows:
if __name__ == '__main__':
    wait_ms = 50
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    parser.add_argument('-w95', '--win95', action='store_true', help='`Windows 95 boot` slow')
    parser.add_argument('-s', '--slow', action='store_true', help='Slow cycle: if you use this with win95 its a medium slow')
    parser.add_argument('-m', '--more', action='store_true', help='More color cycles')
    parser.add_argument('-w', '--white', action='store_true', help='Include the color white in the mix')
    parser.add_argument('-t', '--time', type=int, nargs='?', const=wait_ms, default=50, help='Cycle wait time before rotating a color in ms')
    parser.add_argument('-S', '--steps', type=int, nargs='?', const=STEPS_DEFA, default=0, help='Cycle color change steps')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    wait_ms = args.time
    colors = define_colors(args)
    print("wait_ms " + str(wait_ms))
    try:
        while True:
                if args.slow or args.win95:
                   slow_cycle(strip, args, colors, wait_ms * 2)
                else:
                   default_cycle(strip, colors, wait_ms)
    except KeyboardInterrupt:
         if args.clear:
            colorWipe(strip, Color(0,0,0), 10)
