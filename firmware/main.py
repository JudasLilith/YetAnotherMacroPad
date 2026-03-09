import board
import time

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT


while True:
    print("hello")
    time.sleep(2)
    print("what are you sayin")