from machine import Pin, I2C
from random import choice, randint
from utime import sleep

from rita_facial import RitaFacial
from SSD1306LIB import SSD1306_I2C

ID  = 0
SDA = Pin(16)
SCL = Pin(17)

my_I2C = I2C(id=ID, scl=SCL, sda=SDA)       # type: ignore

OLED = SSD1306_I2C(width=128, height=64, i2c=my_I2C)
OLED.init_display()

rita = RitaFacial(OLED=OLED, inversion=1)

while True:
    for _ in range(randint(1, 4)):
        rita.express("blink")
        sleep(choice([0.1, 0.5, 0.9, 1.5]))
    
    for _ in range(randint(1, 4)):
        rita.express("smile")
        sleep(choice([0.1, 0.5, 0.9, 1.5]))