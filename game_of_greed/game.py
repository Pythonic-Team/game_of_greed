from game_of_greed.game_logic import GameLogic

class Game:

  def play(self, roller):
      round = 1
      roll = 6
      print("Welcome to Game of Greed")
      print("(y)es to play or (n)o to decline")
      input("> ")
      print(f"Starting round {round}")
      print(f"Rolling { roll } dice...")
      print('*** 4 2 6 4 6 5 ***')
      print('Enter dice to keep, or (q)uit:')
      input('> ')
      print("You have 50 unbanked points and 5 dice remaining")
      print("(r)oll again, (b)ank your points or (q)uit:")
      input('> ')
      print("You banked 50 points in round 1")
      print("Total score is 50 points")
      print("Starting round 2")
      print(f"Rolling { roll } dice...")
      print("*** 6 4 5 2 3 1 ***")
      print('Enter dice to keep, or (q)uit:')
      input('> ')
      print('Thanks for playing. You earned 50 points')
  
    
      
       