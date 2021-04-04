from robot import Robot
from pybricks.tools import wait

name = "drive run"

def start():
  Robot.chassis.drive(140, 0)
  wait(2000)
  Robot.brake()

  wait(1000)

  Robot.chassis.drive(-140, 0)
  wait(2000)
  Robot.brake()