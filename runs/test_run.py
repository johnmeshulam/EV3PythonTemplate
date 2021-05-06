from pybricks.tools import wait
from robot import Robot

name = "test run"

def start():
  Robot.screen.print('starting')
  wait(4000)
  Robot.brick.screen.print('ending')