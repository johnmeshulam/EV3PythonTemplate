from robot import Robot
from pybricks.tools import wait

name = "arm run"

def start():
  Robot.arm_left.run_time(180, 3000)
  wait(1000)

  Robot.arm_left.run_time(-180, 3000)