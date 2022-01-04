from dinosaur import Dinosaur
from herd import Herd
from fleet import Fleet
class Battlefield:

  def __init__(self):
    self.fleet = Fleet()
    self.herd = Herd()
    self.user_name = ''

  def run_game(self):
    pass

  def display_welcome(self):
    print('Welcome to Robots vs Dinosaurs!')
    self.user_name = input('Please enter your name to continue: ')
    choose_your_team = ['robots', 'dinosaurs']
    print(input('Your current team is'(choose_your_team)))
    print(input(choose_your_team('Selection'))) 
    if input(choose_your_team) == 'robots':
      print(show_robo_opponent_options)

    else(choose_your_team) == 'dinosaur':
      print(show_dino_opponent_options)

  def battle(self): 
    # when you get robo attack and dino attack wroking do this next
      # start buy writing out the steps on your white board that need to happen for battle to run until all of one team has been eliminated
    pass
  # figure out logic for dino turn and robo turn then call them in battle above 

  def show_dino_opponent_options(self):
    print("Current Dino Herd")
    i = 0 
    for dino in self.herd.dinosaur:
      print(f'Press {i} to select {dino.name} ({dino.health} health)')
      i += 1  
    pass

  def dinosaur_attack(self):
    self.show_dino_opponent_options()
    dino_index = int(input("Select a dinosaur to attack with: "))
    self.show_robo_opponent_options() 
    robo_index = int(input("Select a robot to attack: "))
    print(f'Dinosaur {self.herd.dinosaur[dino_index].name} has been selected to attack {self.fleet.robots[robo_index].name}')
    self.herd.dinosaur[dino_index].attack(self.fleet.robots[robo_index])             
    pass
               

def robo_attack(self):

      self.show_robo_opponent_options()
      robo_index = int(input("Select a robot to attack with: "))
      self.show_dino_opponent_options() 
      dino_index = int(input("Select a dinosaur to attack: "))

      print(f'Robot {self.fleet.robots[robo_index].name} has been selected to attack {self.herd.dinosaur[dino_index].name}')
      self.fleet.robots[robo_index].attack(self.herd.dinosaur[dino_index])             
      pass

def show_robo_opponent_options(self):
    print("Current Robot Fleet:") 
    i = 0
    for robot in self.fleet.robots:
      print(f'Press {i} to select {robot.name} ({robot.health} health)')
      i += 1
    pass




  
def display_winners(self):
    pass
  

  


