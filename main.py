from machine import Pin

from utime import  sleep

ledGreen = Pin(15, Pin.OUT)
ledYellow = Pin(2, Pin.OUT)
ledRed = Pin(0, Pin.OUT)

while True:
    ledGreen.on()
    print("Led ON Green!")
    sleep(20)
    ledGreen.off()
    print("Led OFF!")
    sleep(0.5)

    ledYellow.on()
    print("Led ON Yellow!")
    sleep(10)
    ledYellow.off()
    print("Led OFF!")
    sleep(0.5)

    ledRed.on()
    print("Led ON Red!")
    sleep(7)
    ledRed.off()
    print("Led OFF!")
    sleep(0.5)