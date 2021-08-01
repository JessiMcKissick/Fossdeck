from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 32, i2c)
button1 = Pin(19, Pin.IN, Pin.PULL_DOWN) #Up
button2 = Pin(20, Pin.IN, Pin.PULL_DOWN) #Right
button3 = Pin(18, Pin.IN, Pin.PULL_DOWN) #Down
button4 = Pin(21, Pin.IN, Pin.PULL_DOWN) #Left
button5 = Pin(27, Pin.IN, Pin.PULL_DOWN) #Menu_1 / enter
button6 = Pin(22, Pin.IN, Pin.PULL_DOWN) #Menu_2
button7 = Pin(28, Pin.IN, Pin.PULL_DOWN) #Menu_3
button8 = Pin(26, Pin.IN, Pin.PULL_DOWN) #Menu_4
buzzer = Pin(2, Pin.OUT)

version = 0.1

buzzer_value = 0

