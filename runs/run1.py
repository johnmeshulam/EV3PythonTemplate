from robot import Robot
from pybricks.tools import wait

def start():
  Robot.chassis.drive(70, 0)
  wait(2000)
  Robot.brake()