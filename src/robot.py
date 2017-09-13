from commandbased import CommandBasedRobot


# from commands import AutonomousCommandGroup

class Robot(CommandBasedRobot):
    """
    This main robot class
    """

    def robotInit(self):
        """
        Initializes the robot
        It replaces the constructor for the robot
        :return: void
        """

        # self.autonomous = AutonomousCommandGroup()

        # def autonomousInit(self):
        #     self.autonomousInitialized.start()
