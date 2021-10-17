from collections import Counter
import random 
class GameLogic:
    def __init__(self):
        pass

    @staticmethod
    def calculate_score(dice_roll):
        all_states={
            1:{1:100,2:200,3:1000,4:2000,5:3000,6:4000},
            2:{1:0,2:0,3:200,4:400,5:600,6:800},
            3:{1:0,2:0,3:300,4:600,5:900,6:1200},
            4:{1:0,2:0,3:400,4:800,5:1200,6:1600},
            5:{1:50,2:100,3:500,4:1000,5:1500,6:2000},
            6:{1:0,2:0,3:600,4:1200,5:1800,6:2400},
            7:1500,
            8:0,
            9:1500,
            10:1200
        }

        counter=Counter(dice_roll)
        most_common_result=counter.most_common()
        # return most_common_result
      
    



        # if len(dice_roll)==1 and dice_roll[0]==5: 
        #     return 50
        # if len(dice_roll)==1 and dice_roll[0]==1: 
        #     return 100   


        # target=len(dice_roll)
        # condition=dice_roll[0]==dice_roll[1]  ==dice_roll[2]
        # if  target==3 and condition==1:
        #     return dice_roll[0]*100

        # elif target==3 and condition==2:
        #     return dice_roll[0]*100
        # elif target==3 and condition==3:
        #     return dice_roll[0]*100
        # elif target==3 and condition==4:
        #     return dice_roll[0]*100
        # elif target==3 and condition==5:
        #     return dice_roll[0]*100  
        # elif target==3 and condition==6:
        #     return dice_roll[0]*100 

    @staticmethod
    def roll_dice(rolling):
        """
        Input : is an integer between 1 and 6.
        Output : is a tuple with random values between 1 and 6.
        """
        roll_list = []
        for dice in range(rolling): 
            roll_list.append(random.randint(1,6))

        if len(roll_list)==rolling:
            return tuple(roll_list)  

    
if __name__ == "__main__":
    instance_one=GameLogic()
    # print(instance_one.calculate_score((1,2,4,4,4,5))) 
    print (instance_one.roll_dice(5))
            


