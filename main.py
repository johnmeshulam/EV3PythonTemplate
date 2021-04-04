#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Button
from util import buttons
from robot import Robot
from runs import run1

button_codes = [Button.UP, Button.RIGHT, Button.DOWN, Button.LEFT, Button.CENTER]
button_symbols = [" ^ ", " > ", " v ", " < ", "[] "]
runs = [run1]

def display_menu():
  Robot.brick.screen.clear()

  for i in range(len(runs)):
    Robot.brick.screen.print(button_symbols[i] + runs[i].name)


while True:
  display_menu()

  btn = buttons.wait_for_any_press()
  btn_index = button_codes.index(btn)

  Robot.brick.screen.clear()

  runs[btn_index].start()
