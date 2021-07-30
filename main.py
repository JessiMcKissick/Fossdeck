from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time
import bme280


# Screen is 128 x 32px
# Screen runs on gp0(sda) and gp1(scl)
# Expansion modules run on pins GP3-GP15
# See pi pico pinout for specific pin capabilities
# Modules can only be fed 3.n volts. 5 volt module support may be added in the future with a per-port switch.
# To add an app or module software; Write the module in the dedicated block. In the future apps and module software will be seperate files.
# This is VERY pre-pre-pre-alpha dev software. Don't expect fantastic functionality. Schematics to the device coming soon.
# 3D printing files will also be available soon for a shell.


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

version = 0.1

is_menu = True
is_app_menu = False
is_module_menu = False

menu_item = 0
app_menu_item = 0
module_menu_item = 1

home_items = ["home", "apps", "modules", "info"]
app_list = ["calculator","home"]
module_list = ["home", "emf", "flashlight"]

def startup():
    oled.text("Fossdeck", 16, 0)
    oled.text("Mk0",36,10)
    oled.text("WFX Engineering",0,25)
    oled.show()
    time.sleep(2)
    cls()
    oled.text("v" + str(version), 10, 0)
    oled.show()
    time.sleep(1)

def menu_display():
    cls()
    oled.text(home_items[menu_item], 44, 0)
    if menu_item == 0:
        oled.text(">", 118, 22)
    elif menu_item == len(home_items) - 1:
        oled.text("<", 0, 22)
    else:
        oled.text("<", 0, 22)
        oled.text(">", 118, 22)
    oled.show()

def menu_nav():
    global menu_item
    if button1.value():
        print("up")
    elif button2.value():
        if menu_item < len(home_items) - 1:
            menu_item += 1
            menu_display()
            time.sleep(0.2)
    elif button3.value():
        print("down")
    elif button4.value():
        if menu_item > 0:
            menu_item = menu_item - 1
            menu_display()
            time.sleep(0.2)
    elif button5.value():
        system_menu_master(home_items[menu_item])
    #todo: Add buttons 5-8 and assign functions. On the main menu only 5 does anything (enters into that option)
            #Creat a function that takes whatever current item is shown, then call that function based on the name.
            #EG call menu.items[menu_item] + () or something. So if that expression is saay apps, it'll be apps() 

#######################################################################################################
#APPS BLOCK#########################################################################################
#######################################################################################################
def apps():
    time.sleep(0.2)
    global is_menu
    global is_app_menu
    global app_menu_item
    global app_list
    global is_module_menu
    
    if is_app_menu == False:
        app_menu_display()
    is_app_menu = True
    is_menu = False
    is_module_menu = False
    if button1.value():
        print("up")
    elif button2.value():
        if app_menu_item < len(app_list) - 1:
            app_menu_item += 1
            app_menu_display()
            time.sleep(0.2)
    elif button3.value():
        print("down")
    elif button4.value():
        if app_menu_item > 0:
            app_menu_item = app_menu_item - 1
            app_menu_display()
            time.sleep(0.2)
    elif button5.value():
        system_menu_master(app_list[app_menu_item])
         

def app_menu_display():
    cls()
    oled.text(app_list[app_menu_item], 44, 0)
    if app_menu_item == 0:
        oled.text(">", 118, 22)
    elif app_menu_item == len(app_list) - 1:
        oled.text("<", 0, 22)
    else:
        oled.text("<", 0, 22)
        oled.text(">", 118, 22)
    oled.show()
    
def calculator():
    cls()
    oled.text("Coming soon",0,0)
    oled.show()
    time.sleep(5)
    app_menu_display()
    
#######################################################################################################
#MODULES BLOCK#########################################################################################
#######################################################################################################
def modules():
    time.sleep(0.2)
    global is_menu
    global is_app_menu
    global is_module_menu
    global module_menu_item
    global module_list
    
    if is_module_menu == False:
        module_menu_display()
        is_module_menu = True
        is_app_menu = False
        is_menu = False
    if button1.value():
        print("up")
    elif button2.value():
        if module_menu_item < len(module_list) - 1:
            module_menu_item += 1
            module_menu_display()
            time.sleep(0.2)
    elif button3.value():
        print("down")
    elif button4.value():
        if module_menu_item > 0:
            module_menu_item = module_menu_item - 1
            module_menu_display()
            time.sleep(0.2)
    elif button5.value():
        system_menu_master(module_list[module_menu_item])

def module_menu_display():
    cls()
    oled.text(module_list[module_menu_item], 44, 0)
    if module_menu_item == 0:
        oled.text(">", 118, 22)
    elif module_menu_item == len(module_list) - 1:
        oled.text("<", 0, 22)
    else:
        oled.text("<", 0, 22)
        oled.text(">", 118, 22)
    oled.show()

#######################################################################################################
#INFO BLOCK#########################################################################################
#######################################################################################################


def info():
    cls()
    oled.text("v" + str(version),0,0)
    oled.text("RP2040 CPU",0,10)
    oled.text("1MB flash",0,20)
    oled.show()
    time.sleep(5)
    cls()
    menu_display()


#######################################################################################################
#GENERICS BLOCK#########################################################################################
#######################################################################################################
def cls():    
    oled.fill(0)
    oled.show()

def system_menu_master(inp):
    eval(inp + "()")

def home():
    global is_menu
    global is_app_menu
    global is_module_menu
    is_app_menu = False
    is_menu = True
    is_module_menu = False
    time.sleep(0.2)
    menu_display()



startup()

cls()

menu_display()


while True:
    while is_menu:
        menu_nav()
    while is_app_menu:
        apps()
    while is_module_menu:
        modules()

