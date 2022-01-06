class Robot:
        def __init__(self, name):
            self.name = name
            self.health = 100
            self.weapon = 'Sword', 25

        #this attack funciton will hold the logic for this specific robot to attack a specific dino we pass in when calling the function     EXMPLE robot_one.attack(dino_one)  

        def attack(self, dino):
            self.health = self.health - self.weapon
            print(f'{self.name} has attacked {dino.name} with Sword Slash and did {self.weapon} damage, {dino.name} has {dino.health} remaining')
                
