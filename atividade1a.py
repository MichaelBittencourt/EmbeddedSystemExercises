from gpiozero import LED 
from time import sleep

class LedHz:

    HZ_2 = 2

    def __init__(self, ledPin, frequency):
        self._led = LED(ledPin)
        self._frequency = frequency

    def blinkLed(self):
        self._led.on()
        sleep(1/(2*self._frequency))
        self._led.off()
        sleep(1/(2*self._frequency))

    pass

def main():

    ledHz = LedHz(17, LedHz.HZ_2)

    while True:
        ledHz.blinkLed()

main()
