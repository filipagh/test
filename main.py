from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

led.value(not led.value())
sleep(5.5)
print("ahoj")
