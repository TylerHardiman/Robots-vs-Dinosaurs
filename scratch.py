from dinosaur import Dinosaur
if Dinosaur == 0:
    dinosaur_attack = False
    while dinosaur_attack is False:
      if Dinosaur > 0:
        dinosaur_attack = True
        print('!')
        continue    
    else:    
      Dinosaur == 0
      print('Dinosaurs have lost!')