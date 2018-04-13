#!/usr/bin/env python3

"""
Used to adjust the position of a motor in an already assembled robot
where you can"t move the motor by hand.
"""

from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveDifferential, SpeedRPM
from ev3dev2.wheel import EV3RubberWheel
import argparse
import logging
import sys

# command line args
'''
parser = argparse.ArgumentParser(description="Used to adjust the position of a motor in an already assembled robot")
parser.add_argument("motor", type=str, help="A, B, C or D")
parser.add_argument("degrees", type=int)
parser.add_argument("-s", "--speed", type=int, default=50)
args = parser.parse_args()
'''

# logging
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(levelname)5s: %(message)s")
log = logging.getLogger(__name__)

mdiff = MoveDifferential(OUTPUT_A, OUTPUT_B, EV3RubberWheel, 150)
#mdiff.on_for_distance(500, SpeedRPM(20))

# This goes crazy on brickpi3, does it do the same on ev3?
#mdiff.on_for_distance(500, SpeedRPM(-20))

# Test arc left/right turns
mdiff.on_arc_right(300, 250, SpeedRPM(20))

# Test turning in place
#mdiff.turn_right(90, SpeedRPM(20))
#mdiff.turn_left(90, SpeedRPM(20))


