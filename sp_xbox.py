from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.iodevices import XboxController

hub = PrimeHub()

xbox = XboxController()

while True:

    if Button.A in xbox.buttons.pressed():

        hub.light.on(Color.GREEN)
        xbox.rumble(100, 200)

    elif Button.B in xbox.buttons.pressed():

        hub.light.on(Color.RED)
        xbox.rumble(100, 200)

    elif Button.Y in xbox.buttons.pressed():

        hub.light.on(Color.YELLOW)
        xbox.rumble(100, 200)

    elif Button.X in xbox.buttons.pressed():

        hub.light.on(Color.BLUE)
        xbox.rumble(100, 200)

    else:

        hub.light.off()

