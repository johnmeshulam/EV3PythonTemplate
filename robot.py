# robot.py should not have dependencies outside of pybricks
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import *
from pybricks.tools import wait
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase

constants = {
  "black": 5,
  "white": 60
}

class Robot():

  brick = EV3Brick()

  wheel_left = Motor(Port.B)
  wheel_right = Motor(Port.C)
  chassis = DriveBase(wheel_left, wheel_right,
                      wheel_diameter=54.4, axle_track=108)

  arm_left = Motor(Port.A)
  arm_right = Motor(Port.D)

  gyro = GyroSensor(Port.S1, Direction.COUNTERCLOCKWISE)
  color_left = ColorSensor(Port.S2)
  color_right = ColorSensor(Port.S3)

  @classmethod
  def brake(cls):
    cls.chassis.stop()
    wait(5)
    cls.wheel_left.brake()
    cls.wheel_right.brake()

