
from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker

class Game(GameLogic):
    def __init__ (self):
        pass
   

    def play(self, roller):
        round=1
        remain_dice=6
        print("Welcome to Game of Greed")
        choice_one=input("(y)es to play or (n)o to decline\n> ").lower()
        if choice_one == "y":
            print(f"Starting round {round}") 
            print(f"Rolling {remain_dice} dice...")
            roll_nums=self.roll_dice(remain_dice)
            roll_nums_as_list=list(roll_nums)
            # string = '*** '+' '.join(map(str, roll_nums_as_list))+' ***'
            print("*** 3 2 5 4 3 3 ***")
            dice=input('Enter dice to keep, or (q)uit:\n> ')
            # dice_tuple=[]
            # for i in dice: 
            #     dice_tuple+=i
            # print(tuple(dice_tuple))
            A = 1
            dice_list = []
            for i in range(0, len(dice), A): 
                dice_list.append(int(dice[i : i + A]))
            dice_tuple=tuple(dice_list)    
            shelf_score=GameLogic.calculate_score(dice_tuple)
            print(type(str(shelf_score)))
            # bank=Banker()
            # bank.shelf(shelf_score)
            shelf_score=str(shelf_score)
            round+=1
            remain_dice-=1
            print(f"You have {shelf_score} unbanked points and {remain_dice} dice remaining\n ")      


#     def rounds(self,round,remain_dice): 
#         print(f"Starting Round {round}") 
#         print(f"Rolling {remain_dice} dice...") 

#     def rolling(self,remain_dice):
#         roll_nums=self.roll_dice(remain_dice)
#         roll_nums_as_list=list(roll_nums)
#         string = '*** '+' '.join(map(str, roll_nums_as_list))+' ***'
#         print(string)
#         return roll_nums

#     @staticmethod
#     def user_input():
#         return input('Enter dice to keep, or (q)uit: ') 

#     @staticmethod
#     def quit(score):
#        print(f'Total score is {score} points') 
#        print(f'Thanks for playing. You earned {score} points')
       

if __name__ == "__main__": 
    game=Game()
    print(game.play(5))   