from herd import Herd
from fleet import Fleet

class Battlefield:

  def __init__(self):
      self.team = ''
      self.fleet = Fleet()
      self.herd = Herd()
      

  def run_game(self):
    print(input('Welcome to Robots vs Dinosaurs!'))
    self.battle()
    

  def display_welcome(self):
    print(input('Please type (self team dino) or Dinosaur to select your team!'))


        
      
  def battle(self):
    #while the arrays still have elements in them, battle
    while(len(self.fleet.robots) > 0 and len(self.herd.dinosaur) > 0):
      self.battle()
    
      


    # while(len(self.herd.dinosaur) > 0 and len(self.fleet.robots) > 0):
      # self.dino_turn()


  def dino_turn(self):
    print("Start dino turn")
    self.show_robo_opponents()
    selected_robo = int(input("Select the robot to attack"))
    self.dino_turn(self.fleet.robots[selected_robo])
    

  def robot_turn(self):
    #here is where you will send in the dino being passing in as a param into the attack method in your robot class
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

  # def team_selection():
  #     team_one_dino = Dinosaur
  #     team_two_robo = Robot
  #     choose_your_team = ['Robot', 'Dinosaur']
  #     team_one_dino == True
  #     while team_one_dino is True:
  #       if choose_your_team == Robot:
  #         team_one_dino == False
  #         print(f' Team {team_two_robo}! ')
  #       else:
  #         print(f' Team {team_one_dino}')
  #     pass

  # def robo_and_dino_opponent_options():
  #       show_robo_opponent_options == True
  #       while show_robo_opponent_options is True:
  #         if show_robo_opponent_options == False:
  #             Herd == True
  #             print(input(f'{Dinosaur} is your current team selection and {show_robo_opponent_options}'))
  #         else:
  #           print(input(f'{Robot} is your current team selection and {show_robo_opponent_options}'))
        

  # def battle(): 
    

  #   def show_dino_opponent_options():
  #     print("Current Dino Herd")
  #     i = 0 
  #     for dino in Herd:
  #       print(f'Press {i} to select {dino.name} ({dino.health} health)')
  #       i += 1  
  #     pass

  #   def dinosaur_attack():
  #     show_dino_opponent_options()
  #     dino_index = int(input("Select a dinosaur to attack with: "))
  #     show_robo_opponent_options()
  #     robo_index = int(input("Select a robot to attack: "))
  #     print(f'Dinosaur {Herd[dino_index].name} has been selected to attack {Fleet[robo_index].name}')
  #     Herd[dino_index].attack(Fleet[robo_index])             
  #     pass


  # def show_robo_opponent_options():
  #     print("Current Robot Fleet:") 
  #     i = 0
  #     for robot in Fleet:
  #       print(f'Press {i} to select {robot.name} ({robot.health} health)')
  #       i += 1
  #     pass   

  # def robot_attack():

  #       show_robo_opponent_options()
  #       robo_index = int(input("Select a robot to attack with: "))
  #       show_dino_opponent_options() 
  #       dino_index = int(input("Select a dinosaur to attack: "))

  #       print(f'Robot {Fleet[robo_index].name} has been selected to attack {Herd[dino_index].name}')
  #       Fleet[robo_index].attack(Herd[dino_index])             
  #       pass






    
  def display_winners(self):
      pass
  
    

  


