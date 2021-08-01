#App creation for the fossdeck is simple
#just write the entry point for your software as run()
#then add appname.run to the apps list on main.py, so in this case test_program.run
#this will be run as a function when launched.
#once the app ends, the system will return you to the app or module menu.
#Don't forget to import your app to main!
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time
import var
import LED


i = 0

def run():
    print("print systems OK")
    var.oled.fill(0)
    var.oled.text("LED test",0,0)
    LED.green()
    LED.red()
    var.oled.show()
    time.sleep(3)
    LED.off("g")
    time.sleep(1)
    LED.off("r")
    var.oled.fill(0)
    var.oled.text("test complete", 0,0)
    var.oled.show()
    time.sleep(3)