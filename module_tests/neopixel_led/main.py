from machine import Pin, ADC
import time
import neopixel as np


led = Pin(13, Pin.OUT)
pin = Pin(7)
neo_leds = np.NeoPixel(pin, 8)

while True:
    print("loop")
    led.value(not led.value())
    neo_leds[0] = (255, 0, 0)
    neo_leds[1] = (0, 255, 0)
    neo_leds.write()

    time.sleep(3)

    led.value(not led.value())
    neo_leds[0] = (0, 255, 0)
    neo_leds[1] = (0, 0, 0)
    neo_leds.write()

    time.sleep(3)



