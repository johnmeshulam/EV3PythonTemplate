# robot.py should not have dependencies outside of pybricks
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import *
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase

constants = {
  "black": 5,
  "white": 70
}

class Robot():

  brick = EV3Brick()

  wheel_left = Motor(Port.B)
  wheel_right = Motor(Port.C)
  chassis = DriveBase(wheel_left, wheel_right,
                      wheel_diameter=62.4, axle_track=100)

  arm_left = Motor(Port.A)
  arm_right = Motor(Port.D)

  gyro = GyroSensor(Port.S1, Direction.COUNTERCLOCKWISE)
  color_left = ColorSensor(Port.S2)
  color_right = ColorSensor(Port.S4)

  @classmethod
  def brake(cls):
    cls.chassis.stop()
    cls.wheel_left.brake()
    cls.wheel_right.brake()

  @classmethod
  def reset_gyro(cls):
    cls.gyro.reset_angle(0)
    cls.gyro.speed()
    cls.gyro.angle()
