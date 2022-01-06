# def robo_and_dino_opponent_options():
#       show_robo_opponent_options == True
#       while show_robo_opponent_options is True:
#         if show_robo_opponent_options == False:
#             Herd == True
#             print(input(f'{Dinosaur} is your current team selection and {show_robo_opponent_options}'))
#         else:
#           print(input(f'{Robot} is your current team selection and {show_robo_opponent_options}'))
from battlefield import Battlefield

battlefield = Battlefield()
battlefield.run_game()
battlefield.display_welcome()
battlefield.battle()
battlefield.show_robo_opponents()
battlefield.dino_turn()
battlefield.show_dino_opponents()
battlefield.robot_turn()
battlefield.display_winners()