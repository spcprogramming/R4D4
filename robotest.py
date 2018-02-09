from breezycreate2 import _Create2
import time

# A simple melody that plays every time the bot is connected to.
MELODY = [('C4',11,0.3),
            ('C4',11,0.3),
            ('C4',11,0.3),
            ('C4',32,0.7),
            ('G4',32,0.7),
            ('F4',11,0.3),
            ('E4',11,0.3),
            ('D4',11,0.3),
            ('C5',64,1.2),
            ('G4',40,0.7),
            ('F4',11,0.3),
            ('E4',11,0.3),
            ('D4',11,0.3),
            ('C5',64,1.2),
            ('G4',40,0.7),
            ('F4',11,0.3),
            ('E4',11,0.3),
            ('F4',11,0.3),
            ('D4',64,2) ]


class SillyRobot:

    def __init__(self):
        self.robot = _Create2('COM3', 115200) # Connect to the bot through the serial connection
        for triple in MELODY: # Play a simple melody
            self.robot.play_note(triple[0], triple[1])
            time.sleep(triple[2])

    def close(self):
        """Closes connection to robot"""
        self.robot.destroy()

    def move(self, speed, sleep):
        """Sends move command to robot to move forward or backward
        Speed: -500 to 500
        sleep: How long the robot should move"""
        self.robot.drive(speed, 0) # Moves the robot forward at the specified speed
        time.sleep(sleep) # Sleep while the robot moves
        self.robot.drive(0, 0) # Stops the robot

    def turn(self, speed, direction, sleep):
        """Sends move command to robot to run
        speed: 0 to 500
        dir: -1(CW) to 1(CCW)
        sleep: How long the robot should turn
        """
        if speed < 0: # If the speed input is below 0
            speed = abs(speed)
        self.robot.drive(speed, direction) # Have the robot turn a certain direction at a certain speed
        time.sleep(sleep) # Sleep while the robot turns
        self.robot.drive(0, 0) # Stop the robot


robot = SillyRobot() # Create a new robot

robot.move(100, 2) # Move the bot forward
robot.turn(100, -1, 1) # Turn the bot clockwise
robot.move(-100, 2) # Move the bot backwards
robot.close() # Close the connection
