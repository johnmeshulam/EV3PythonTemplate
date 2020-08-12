from pybricks.parameters import Button
from pybricks.tools import wait
from robot import Robot, constants
from util import buttons

#TODO: make this normal because its cancer right now
def align(drive_speed, align_speed):
  threshold = 5
  target = constants["black"] + threshold

  left_value, right_value = _read_sensors()

  if(not (right_value <= target or left_value <= target)):
    Robot.chassis.drive(drive_speed, 0)
  while(not (right_value <= target or left_value <= target)):
    left_value, right_value = _read_sensors()
  Robot.brake()

  if(not (right_value <= target and left_value <= target)):
    if(right_value <= target):
      Robot.wheel_left.run(align_speed)
    elif(left_value <= target):
      Robot.wheel_right.run(align_speed)
    while(not (right_value <= target and left_value <= target)):
      left_value, right_value = _read_sensors()

  Robot.brake()

def _read_sensors():
    right_value = Robot.color_right.reflection()
    left_value = Robot.color_left.reflection()
    return (left_value, right_value)

#TODO: for higher level - create 'side; enum and pass is instead of sensor, add 'line side' parameter
def follow_distance(distance, sensor, speed, kp):
  Robot.chassis.reset()
  target = (constants["black"] + constants["white"]) / 2

  while Robot.chassis.distance() < distance:
    error = sensor.reflection() - target
    turn = error * kp
    Robot.brick.screen.print(Robot.chassis.distance())
    Robot.chassis.drive(speed, turn)

    wait(10)

  
  Robot.brake()

def reset():
  Robot.brick.screen.clear()

  Robot.brick.screen.draw_text(0, 0, "reset black")
  buttons.wait_for_press(Button.CENTER)
  Robot.black = Robot.color_left.reflection()

  Robot.brick.screen.draw_text(120, 0, str(Robot.black))
  Robot.brick.screen.draw_text(0, 20, "reset white")
  buttons.wait_for_press(Button.CENTER)
  Robot.white = Robot.color_left.reflection()

  Robot.brick.screen.draw_text(120, 20, str(Robot.white))
  buttons.wait_for_press(Button.CENTER)


