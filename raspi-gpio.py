from gpiozero import LED
from time import sleep

#while True:

led = LED(17)

while True:
    print("on")
    led.on()
    sleep(1)
    print("off")
    led.off()
    sleep(1)