from machine import Pin, I2C

LED1 = Pin(16, Pin.OUT)
LED2 = Pin(17, Pin.OUT)

def green():
    LED2.on()

def red():
    LED1.on()
    
def off(c):
    if c == "g" or c == "green":
        LED2.off()
    elif c == "r" or c == "red":
        LED1.off()
    else:
        LED1.off()
        LED2.off()