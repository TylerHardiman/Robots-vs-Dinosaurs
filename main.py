from herd import Herd
from fleet import Fleet
from battlefield import Battlefield

battlefield = Battlefield()
battlefield.run_game()
battlefield.display_welcome()
battlefield.dinosaur_attack()
if Herd == 0:
    dinosaur_attack = False
    while dinosaur_attack is False:
      if Herd > 0:
        dinosaur_attack = True
        print('!')
        continue    
    else:    
      Herd == 0
      print('Dinosaurs have lost!')

battlefield.robo_attack
if len(Fleet()) == 0:
      robo_attack = False
while robo_attack is False:
      if Fleet() > 0:
        robo_attack = True
        print('!')
        continue    
else:    
      Fleet() == 0
      print('Robots have lost!')
battlefield.show_robo_opponent_options()
battlefield.show_dino_opponent_options()