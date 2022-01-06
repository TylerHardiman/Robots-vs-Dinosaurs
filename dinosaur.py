class Dinosaur:
        def __init__(self, name):
            self.name = name
            self.health = 100
            self.attack_power = 25

        def attack(self, robot):
            self.robot = self.robot - self.attack_power
            print(f'{self.name} has attacked {robot} and did {self.attack_power} damage, {robot.name} has {robot.health} remaining')
            





