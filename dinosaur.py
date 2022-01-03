from weapon import Weapon

class Dinosaur:
        def __init__(self, name):
            self.name = name
            self.health = 100
            self.attack_power = 25
            self.weapon = Weapon("Claws", 25)


        #this attack funciton will hold the logic for this specific robot to attack a specific dino we pass in when calling the function     EXMPLE robot_one.attack(dino_one)
        def attack(self, robot):
            print(self.weapon.attack_power)
            pass





