from robot import Robot
class Fleet:
        def __init__(self):
            self.robots = []
            self.create_fleet()

        def create_fleet(self):
            robot_one = Robot("WALL-E")
            robot_two = Robot("Marvin the Android")
            robot_three = Robot("The Iron Giant")

            self.robots.append(robot_one)
            self.robots.append(robot_two)
            self.robots.append(robot_three)