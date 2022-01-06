class Robot:
        def __init__(self, name):
            self.name = name
            self.health = 100
            self.weapon = 'Sword', 25

        def attack(self, dino):
            self.health = self.health - self.weapon
            print(f'{self.name} has attacked {dino.name} with Sword Slash and did {self.weapon} damage, {dino.name} has {dino.health} remaining')
                
