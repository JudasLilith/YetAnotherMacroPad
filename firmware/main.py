import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import digitalio
import analogio
import board

TopLeft = digitalio.DigitalInOut(board.D10)
TopLeft.direction = digitalio.Direction.INPUT
TopLeft.pull = digitalio.Pull.UP

TopRight = digitalio.DigitalInOut(board.D7)
TopRight.direction = digitalio.Direction.INPUT
TopRight.pull = digitalio.Pull.UP

BotLeft = digitalio.DigitalInOut(board.D8)
BotLeft.direction = digitalio.Direction.INPUT
BotLeft.pull = digitalio.Pull.UP

BotRight = digitalio.DigitalInOut(board.D9)
BotRight.direction = digitalio.Direction.INPUT
BotRight.pull = digitalio.Pull.UP

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

    

while True:

    print(str(TopLeft.value) + " " + str(TopRight.value) + " " + str(BotLeft.value) + " " + str(BotRight.value))


    if TopRight.value == False:
        kbd.send(Keycode.CONTROL, Keycode.S)
        time.sleep(0.1)

    if TopLeft.value == False:
        kbd.send(Keycode.CONTROL, Keycode.Z)
        time.sleep(0.2)

    if BotLeft.value == False:
        kbd.send(Keycode.CONTROL, Keycode.Y)
        time.sleep(0.2)

    if BotRight.value == False:
        kbd.send(Keycode.CONTROL, Keycode.R)
        time.sleep(0.2)
