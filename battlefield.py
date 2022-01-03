from herd import Herd
from fleet import Fleet

class Battlefield:

  def __init__(self):
    self.fleet = Fleet()
    self.herd = Herd()
    self.user_name = ""

  def run_game(self):
    self.display_welcome()
    pass

  def display_welcome(self):
    print('Welcome to Robots vs Dinosaurs!')
    self.user_name = input('Please enter your name to continue: ')
    pass

  def battle(self):
    pass
  # figure out logic for dino turn and robo turn then call them in battle above 
  def dino_turn(self, dinosaur):
    pass

  def robo_turn(self, robot):
    pass

  def show_dino_opponent_options(self):
    pass

  def show_robo_opponent_options(self):
    pass
  
  def display_winners(self):
    pass
  

  


