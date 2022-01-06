from herd import Herd
from fleet import Fleet

choose_your_team = ['robots', 'dinosaurs']

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
    
    print(input(choose_your_team('robots', 'dinosaurs'))) 
    print(input(f'{choose_your_team} is your current team selection'))

    choose_your_team == 'robots'
    show_robo_opponent_options == True
    while show_robo_opponent_options is True:
      if choose_your_team == 'dinosaurs':
        show_robo_opponent_options == False
        print(input(f'{choose_your_team} is your current team selection'))
      else:
          print(input(f'{choose_your_team} is your current team selection'))
      pass


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



      from fleet import Fleet
  from herd import Herd
  from robot import Robot
  if len(Herd) == 1:
    if Fleet() == 0:
        print('Robots have lost!')
    else:    
      def attack(self, robot):
            self.robot = self.robot - self.attack_power
            print(f'{self.name} has attacked {robot} and did {self.attack_power} damage, {robot.name} has {robot.health} remaining')
          elif
      def attack(self, dino):
            self.health = self.health - Weapon
            print(f'{self.name} has Sword Attack on {dino} and did {Weapon} damage, {dino.name} has {dino.health} remaining')
     #when you get robo attack and dino attack wroking do this next
      # start buy writing out the steps on your white board that need to happen for battle to run until all of one team has been eliminated


      if self.robot_turn == True:
          self.dino_turn = False
          print(self.robot_turn())
          break
      else:
          self.dino_turn == True
          print(self.dino_turn())
           if (self.fleet.robots) > 0 or len(self.herd.dinosaur) > 0:
        print(self.battle((self)))
        break

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


