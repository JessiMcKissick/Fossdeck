# Fossdeck
## Warning: This project is still relatively young. Software will be buggy and hardware may be flawed.
### An open-source modular system for science and fun based on the RP2040 platform and micropython.

## The hardware
The hardware consists of a handful of simple components:
1. Raspberry Pi Pico (or compatible microcontroller)
2. SSD1306 oled display (128x32)
3. Some perfboard and momentary switches to create a control board
4. A diy power junction to connect various things to
5. 1100+ mah lipo battery
6. lipo charge controller
7. Wire (duh)
8. A toggle switch to control power from the charge controller to the device

(Pictures and schematic coming soon)

## Flashing the software
To install the operating system to your fossdeck:
1. Install Thonny
2. Open the main.py file in thonny
3. Plug in your fossdeck
4. In the bottom right of thonny, click "default"
5. Select micropython
6. Select install
7. Once completed, press the play icon in thonny
8. Select pi pico on the popup
9. Thonny will flash the OS to your fossdeck
10. Check your fossdeck's screen. If nothing shows up, check all of your hardware connections and ensure you connected everything to the correct pins.


## Creating modules
The fossdeck is designed with 2 easily accessible expansion ports for various sorts of modules. 
| Slot | Pins                          | Capabilities                                                       |
|------|-------------------------------|--------------------------------------------------------------------|
| 1    | GP3 GP4 GP5 GP6 GP7 GP8       | SPIO (SCK,TX,RC,CSN), I2C1 SDA/SCL, I2C0 SDA/SCL, UART1 TX/RX, PWM |
| 2    | GP10 GP11 GP12 GP13 GP14 GP15 | SPIO (SCK,TX,RC,CSN), I2C1 SDA/SCL, I2C0 SDA/SCL, UART1 TX/RX, PWM |
| Both | 3v3 GND                       |                                                                    |

(Pinout of expansion slots will be found here in the future)




