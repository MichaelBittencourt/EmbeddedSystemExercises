import time
from gpiozero import PWMLED

# To get a single character from standard input.
# Does not show anything to the screen.
class _Getch:

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


getch = _Getch()

pwmOutput = PWMLED(17)

intensity = 0
limitUp = 1.0
limitDown = 0
step = 0.05

while True:
    character = getch()
    value = 0
    if character == 'h':
        value = step
    elif character == 'l':
        value = -step
    elif character == 'q':
        exit(0)
    
    if value != 0:
        oldPosition = intensity
        intensity = intensity + value
        intensity = limitUp if intensity > limitUp else limitDown if intensity < limitDown else intensity
        print("will show intensity: ", intensity)
        if oldPosition != intensity:
            pwmOutput.value = intensity
