from robot import Robot
from pybricks.tools import wait

name = "test run"

def start():
  Robot.chassis.drive(70, 0)
  wait(2000)
  Robot.brake()

  Robot.chassis.drive(-70, 0)
  wait(2000)
  Robot.brake()