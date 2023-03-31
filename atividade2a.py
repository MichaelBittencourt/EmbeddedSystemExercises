import time
from gpiozero import PWMLED

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

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


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()


pwmOutput = PWMLED(17)

intensity = 0
limitUp = 1.0
limitDown = 0

while True:
    character = getch()
    value = 0
    if character == 'h':
        value = 0.1
    elif character == 'l':
        value = -0.1
    elif character == 'q':
        exit(0)
    
    if value != 0:
        oldPosition = intensity
        intensity = intensity + value
        intensity = limitUp if intensity > limitUp else limitDown if intensity < limitDown else intensity
        print("will show intensity: ", intensity)
        if oldPosition != intensity:
            pwmOutput.value = intensity
