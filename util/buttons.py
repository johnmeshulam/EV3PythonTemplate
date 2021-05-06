from pybricks.parameters import Button
from pybricks.tools import wait
from robot import Robot

def button_pressed(btn):
  if type(btn) == tuple:
    print([True for b in btn if b in Robot.brick.buttons.pressed()])
    return len([True for b in btn if b in Robot.brick.buttons.pressed()]) == len(btn)
  return btn in Robot.brick.buttons.pressed()

def wait_for_press(btn):
  while(not button_pressed(btn)):
    pass

  while(button_pressed(btn)):
    pass

  wait(100)

def wait_for_any_press():
  while(not len(Robot.brick.buttons.pressed()) == 1):
    pass

  btn = Robot.brick.buttons.pressed()[0]

  while(button_pressed(btn)):
    pass
  
  wait(100)

  return btn
