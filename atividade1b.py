from gpiozero import LED, Button
from time import sleep

class LedKey:

    HZ_2 = 2
    HZ_1 = 1

    def __init__(self, ledPin, buttonPin):
        self._led = LED(ledPin)
        self._button = Button(buttonPin)
        self._frequency = LedKey.HZ_1


    def checkButton(self):
        if self._button.is_pressed:
            self._frequency = LedKey.HZ_2 if self._frequency is LedKey.HZ_1 else LedKey.HZ_1

    def blinkLed(self):
        self._led.on()
        sleep(1/(2*self._frequency))
        self._led.off()
        sleep(1/(2*self._frequency))

    pass

def main():

    ledKey = LedKey(17, 2)

    while True:
        ledKey.checkButton()
        ledKey.blinkLed()

main()
