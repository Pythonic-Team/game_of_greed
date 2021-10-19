
from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
# from game_logic import GameLogic
# from banker import Banker
from collections import Counter


class Game():
    def __init__(self):
        self.round = 1
        self.remain_dice = 6
        self.str_dice = ''
        self.fire = False
        self.cheated=False

    def play(self, roller=GameLogic.roll_dice):
        print("Welcome to Game of Greed\n(y)es to play or (n)o to decline")
        choice = input('> ').lower()
        if choice != 'n' or not 'q':
            self.fire = True
        banker = Banker()
        while self.fire:
            print(f'Starting round {self.round}')
            while True:
                if not self.cheated:
                    print(f"Rolling {self.remain_dice} dice...")
                dice = roller(self.remain_dice)
                self.str_dice = ' '.join(map(str, dice))
                print(f'*** {self.str_dice} ***')
                print('Enter dice to keep, or (q)uit:')
                prompt = input("> ").lower()
                if prompt == 'q' or prompt == 'quit':
                    print(
                        f"Thanks for playing. You earned {banker.balance} points")
                    return
                else:
                    shelf = [int(n) for n in prompt if n != ' ']
                    current_dice = Counter(dice)
                    if not GameLogic.validate_keepers(current_dice, shelf):
                        print("Cheater!!! Or possibly made a typo...")
                        self.cheated = True
                        continue
                    banker.shelf(GameLogic.calculate_score(shelf))
                    print(
                        f"You have {banker.shelved} unbanked points and {len(dice) - len(shelf)} dice remaining")
                    print("(r)oll again, (b)ank your points or (q)uit:")
                    prompt = input("> ")
                    if prompt == "b":
                        self.remain_dice = len(dice) - len(shelf)
                        print(
                            f"You banked {banker.shelved} points in round {self.round}")
                        banker.bank()
                        print(f"Total score is {banker.balance} points")
                        self.round += 1
                        self.remain_dice = 6
                        break
                    elif prompt == 'r':
                        self.remain_dice = len(dice) - len(shelf)
                        if not self.remain_dice:
                            self.remain_dice = 6
                            continue
                        continue
                    elif prompt == 'q':
                        print(
                            f"Thanks for playing. You earned {banker.balance} points")
        print('OK. Maybe another time')


if __name__ == "__main__":
    g = Game()
    g.play()
