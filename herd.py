from dinosaur import Dinosaur
class Herd:
        def __init__(self):
            self.dinosaur = []
            self.create_herd()
            self.attack_power = 25
            
        def create_herd(self):
            dinosaur_one = Dinosaur("Blue")
            dinosaur_two = Dinosaur("Spots")
            dinosaur_three = Dinosaur("Cuddles")

            self.dinosaur.append(dinosaur_one)
            self.dinosaur.append(dinosaur_two)
            self.dinosaur.append(dinosaur_three)

        