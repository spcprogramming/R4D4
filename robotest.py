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
        self.robot = _Create2('COM3', 115200)  # Connect to the bot through the serial connection
        self.robot.full()  # Put the robot in full mode
        self.robot.digit_led_ascii('R4D4')  # Displays the string on the robot's display
        for triple in MELODY:  # Play a simple melody
            self.robot.play_note(triple[0], triple[1])
            time.sleep(triple[2])

    def close(self):
        """Closes connection to robot"""
        self.robot.digit_led_ascii("    ")  # Clears the led display
        self.robot.destroy()

    def move(self, speed, sleep):
        """Sends move command to robot to move forward or backward
        Speed: -500 to 500
        sleep: How long the robot should move"""
        self.robot.drive(speed, 0)  # Moves the robot forward at the specified speed
        time.sleep(sleep)  # Sleep while the robot moves
        self.robot.drive(0, 0)  # Stops the robot

    def turn(self, speed, direction, sleep):
        """Sends move command to robot to run
        speed: 0 to 500
        dir: -1(CW) to 1(CCW)
        sleep: How long the robot should turn
        """
        if speed < 0:  # If the speed input is below 0
            speed = abs(speed)
        self.robot.drive(speed, direction)  # Have the robot turn a certain direction at a certain speed
        time.sleep(sleep)  # Sleep while the robot turns
        self.robot.drive(0, 0)  # Stop the robot

    def enable_motors(self, main_speed, side_speed, vacuum_speed):
        """Turns the motors on in the rear of the robot
        main_speed: Main Brush, -127 to 127, Positive spins inward
        side_speed: Side Brush, -127 to 127, Positive speeds spin counterclockwise
        vacuum_speed: Vacuum, 0 to 127, No Negative speeds allowed
        """
        if vacuum_speed < 0:
            vacuum_speed = abs(vacuum_speed)
        self.robot.motors_pwm(main_speed, side_speed, vacuum_speed)

    def disable_motors(self):
        """Turns the motors off in the rear of the robot"""
        self.robot.motors_pwm(0, 0, 0)

    def set_led(self, display_string):
        """Sets the robots led display
        Must be 4 characters long
        Space is represented by ' '"""
        self.robot.digit_led_ascii(display_string)


def test_move(bot):
    bot.move(100, 2)  # Move the bot forward
    bot.turn(100, -1, 1)  # Turn the bot clockwise
    bot.move(-100, 2)  # Move the bot backwards


def test_motors(bot):
    bot.enable_motors(127, 127, 127)  # Turn the motors on
    time.sleep(2)  # Sleep for 2 seconds
    bot.disable_motors()  # Turn motors off


def main():
    robot = SillyRobot()  # Create a new robot
    selection = 'n'  # Sentinel variable

    while selection != 'q':
        print("Select an option\n"  # Display a small menu
              "1: Test Movement\n"
              "2: Test Motors\n"
              "Q: Quit")

        selection = input()  # Get input
        print(selection)

        if selection == '1':  # Move the robot
            test_move(robot)
        elif selection == '2':  # Enable the motors
            test_motors(robot)
        elif selection == 'q' or selection == 'Q':  # Quit
            selection = selection.lower()
            print("Thanks for trying out the robot!")
        else:  # Invalid input
            print("Invalid input. Please try again.")

    robot.close()  # Close the connection


main()
