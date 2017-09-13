from wpilib.command.command import Command

from ... import operatorinput
from ... import subsystems


class FollowJoystick(Command):
    """
    todo
    """

    def __init__(self):
        """
        todo
        """
        super().__init__(self, 'Follow Joystick')
        self.requires(subsystems.drivetrain)

    def initialize(self):
        """
        todo
        :return:
        """
        pass

    def execute(self):
        """
        todo
        :return:
        """
        x = operatorinput.joystick.getX()
        y = operatorinput.joystick.getY()

        subsystems.drivetrain.drive(x, y)

    def isFinished(self):
        """
        todo
        :return: boolean
        """
        return super().isFinished()
