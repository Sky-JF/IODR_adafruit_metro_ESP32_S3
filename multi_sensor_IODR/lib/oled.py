
import qwiic_oled
import sys

userOLED = qwiic_oled.QwiicLargeOled()
_initialized = False

# Initialize
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

# Clear the OLED screen
def clear():
    if not _initialized:
        return

    userOLED.clear(userOLED.ALL)
    userOLED.display()

# Write any message to the whole OLED
def write(message):
    if not _initialized:
        print("Call oled_init() first", file=sys.stderr)
        return

    userOLED.clear(userOLED.PAGE)
    userOLED.print(message)
    userOLED.display()


