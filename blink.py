from machine import Pin
from utime import sleep

red = Pin(18, Pin.OUT)
yellow = Pin(19, Pin.OUT)
blue = Pin(20, Pin.OUT)


while True:
    red.toggle()
    sleep(1)
    yellow.toggle()
    sleep(1)
    blue.toggle()
    sleep(1)
