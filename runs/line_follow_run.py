from robot import Robot
from pybricks.tools import wait
from util import light

name = "line follow"

def start():
  light.follow_distance(500, Robot.color_right, speed=100, kp=1.5)