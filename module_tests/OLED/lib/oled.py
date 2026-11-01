
import qwiic_oled
import sys

from machine import Pin, I2C

i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)
print(i2c.scan())

userOLED = qwiic_oled.QwiicLargeOled()
_initialized = False


def init():
    global _initialized

    if not userOLED.connected:
        print("OLED is not connected", file=sys.stderr)
        return False

    userOLED.begin()
    userOLED.clear(userOLED.ALL)
    userOLED.display()

    _initialized = True
    return True


def clear():
    if not _initialized:
        return

    userOLED.clear(userOLED.ALL)
    userOLED.display()


def write(message):
    if not _initialized:
        print("Call oled_init() first", file=sys.stderr)
        return

    userOLED.clear(userOLED.PAGE)
    userOLED.print(message)
    userOLED.display()


