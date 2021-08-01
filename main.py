from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time
import bme280
import LED #LED systems
import var #Common variables
import test_program #A simple hardware test program
import gen #Generic functions
import calculator


# Screen is 128 x 32px
# Screen runs on gp0(sda) and gp1(scl)
# Expansion modules run on pins GP3-GP15 (excluding gp9)
# See pi pico pinout for specific pin capabilities
# Modules can only be fed 3.n volts. 5 volt module support may be added in the future with a per-port switch.
# To add an app or module software; Write the module in the dedicated block. In the future apps and module software will be seperate files.
# This is VERY pre-pre-pre-alpha dev software. Don't expect fantastic functionality. Schematics to the device coming soon.
# 3D printing files will also be available soon for a shell.



is_menu = True
is_app_menu = False
is_module_menu = False

menu_item = 0
app_menu_item = 1
module_menu_item = 0

home_items = ["home", "apps", "modules", "info"]
app_list = ["home", "calculator.run", "test_program.run"]
module_list = ["home"]

def startup():
    var.oled.text("Fossdeck", 16, 0)
    var.oled.text("Mk0",36,10)
    var.oled.text("WFX Engineering",0,25)
    var.oled.show()
    LED.green()
    time.sleep(2)
    gen.cls()
    var.oled.text("v" + str(var.version), 10, 0)
    var.oled.show()
    time.sleep(1)
    LED.red()
    time.sleep(0.2)
    LED.off(0)
    
def menu_display():
    gen.cls()
    var.oled.text(home_items[menu_item], 44, 0)
    if menu_item == 0:
        var.oled.text(">", 118, 22)
    elif menu_item == len(home_items) - 1:
        var.oled.text("<", 0, 22)
    else:
        var.oled.text("<", 0, 22)
        var.oled.text(">", 118, 22)
    var.oled.show()

def menu_nav():
    global menu_item
    if var.button1.value():
        print("up")
    elif var.button2.value():
        if menu_item < len(home_items) - 1:
            menu_item += 1
            menu_display()
            time.sleep(0.2)
    elif var.button3.value():
        print("down")
    elif var.button4.value():
        if menu_item > 0:
            menu_item = menu_item - 1
            menu_display()
            time.sleep(0.2)
    elif var.button5.value():
        gen.smm(home_items[menu_item])
    #todo: Add var.buttons 5-8 and assign functions. On the main menu only 5 does anything (enters into that option)
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
    if var.button1.value():
        print("up")
    elif var.button2.value():
        if app_menu_item < len(app_list) - 1:
            app_menu_item += 1
            app_menu_display()
            time.sleep(0.2)
    elif var.button3.value():
        print("down")
    elif var.button4.value():
        if app_menu_item > 0:
            app_menu_item = app_menu_item - 1
            app_menu_display()
            time.sleep(0.2)
    elif var.button5.value():
        gen.smm(app_list[app_menu_item])
        if app_list[app_menu_item] is not "home":
            app_menu_display()
         

def app_menu_display():
    gen.cls()
    var.oled.text(app_list[app_menu_item], 0, 0)
    if app_menu_item == 0:
        var.oled.text(">", 118, 22)
    elif app_menu_item == len(app_list) - 1:
        var.oled.text("<", 0, 22)
    else:
        var.oled.text("<", 0, 22)
        var.oled.text(">", 118, 22)
    var.oled.show()
    
    
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
    if var.button1.value():
        print("up")
    elif var.button2.value():
        if module_menu_item < len(module_list) - 1:
            module_menu_item += 1
            module_menu_display()
            time.sleep(0.2)
    elif var.button3.value():
        print("down")
    elif var.button4.value():
        if module_menu_item > 0:
            module_menu_item = module_menu_item - 1
            module_menu_display()
            time.sleep(0.2)
    elif var.button5.value():
        gen.smm(module_list[module_menu_item])
        if module_list[module_menu_item] is not "home":
            module_menu_display()

def module_menu_display():
    gen.cls()
    var.oled.text(module_list[module_menu_item], 0, 0)
    if module_menu_item == 0:
        var.oled.text(">", 118, 22)
    elif module_menu_item == len(module_list) - 1:
        var.oled.text("<", 0, 22)
    else:
        var.oled.text("<", 0, 22)
        var.oled.text(">", 118, 22)
    var.oled.show()

#######################################################################################################
#INFO BLOCK#########################################################################################
#######################################################################################################


def info():
    gen.cls()
    LED.green()
    var.oled.text("v" + str(var.version),0,0)
    var.oled.text("RP2040 CPU",0,10)
    var.oled.text("1MB flash",0,20)
    var.oled.show()
    time.sleep(5)
    gen.cls()
    LED.off(0)
    menu_display()


#######################################################################################################
#GENERICS BLOCK#########################################################################################
#######################################################################################################

#Generics that haven't been moved to gen

def home():
    global is_menu
    global is_app_menu
    global is_module_menu
    is_app_menu = False
    is_menu = True
    is_module_menu = False
    time.sleep(0.2)
    menu_display()
    



#######################################################################################################
#FLOW BLOCK############################################################################################
#######################################################################################################


startup()

gen.cls()

menu_display()


while True:
    while is_menu:
        menu_nav()
    while is_app_menu:
        apps()
    while is_module_menu:
        modules()
