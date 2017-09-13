from wpilib.joystick import Joystick

from . import config

joystick = None


def init():
    """
    todo
    :return:
    """
    global joystick

    joystick = Joystick(6, config.config.robotmap.joystick.port)
