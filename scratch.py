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