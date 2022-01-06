from herd import Herd
from fleet import Fleet
dinosaurs = True
robots = False
dino_turn = True
robo_turn = False

class Battlefield:

  def __init__(self):
      self.team = ''
      self.fleet = Fleet()
      self.herd = Herd()
      

  def run_game(self):
    print(input('Welcome to Robots vs Dinosaurs!'))
    

  def display_welcome(self):
    (input('Please type Robots or Dinosaurs to select your team!: '))

             
  def battle(self):
    robo_turn = True
    while(len(self.fleet.robots) > 0 and len(self.herd.dinosaur) > 0) is True:
      if robo_turn == True:
        (robot_turn)
        print('Robots have the field!')
        break
      else:
        print('Dinosaurs have the field!')
        self.battle()
        continue

  def dino_turn(self):
    print("Start dino turn")
    self.show_robo_opponents()
    selected_robo = int(input("Select the robot to attack"))
    self.dino_turn[selected_robo]
    

  def robot_turn(self):
    print("Start robot turn")
    self.show_dino_opponents()
    selected_dino = int(input("Select the dino to attack"))
    self.robot_turn(self.herd.dinosaur[selected_dino])
   

  def show_dino_opponents(self):
    print("Current Herd:")
    i = 0
    for dino in self.herd.dinosaur:
      print(f"Press {i} to select {dino.name}")
      i +=1

  def show_robo_opponents(self):
    print("Current fleet: ")
    i=0
    for robots in self.fleet.robots:
      print(f"Press {i} to select {robots.name}")
      i +=1

def display_winners(self):
      if Fleet == 0:
        print('Dinosaurs have won!')
      else:
        print('Robots have won!')
        

 



    
  
  
    

  


