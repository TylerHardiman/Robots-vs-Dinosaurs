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

        # def attack(self, dino):
        #     self.health = self.health - Weapon
        #     print(f'{self.name} has Sword Attack on {dino} and did {Weapon} damage, {dino.name} has {dino.health} remaining')
        # def attack(self, dino):
        #     self.health = self.health - self.weapon
        #     print(f'{self.name} has attacked {dino.name} with Sword Slash and did {self.weapon} damage, {dino.name} has {dino.health} remaining')

       
                
