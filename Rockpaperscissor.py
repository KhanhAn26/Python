import random

def Menu():
    print("**************")
    print("Welcome!")
    print("What do you want to do?")
    print("1. Have a rock-paper-scissor battle with bot")
    print("2. Quit")
    print("**************")
    while True:
     tra_loi=input()
     if tra_loi in ["1","2"]:
         return tra_loi
     else:
         print("Invalid. Please try again!")
        
        

def Rockpaperscissor():
    player=input("Enter 1 for scissor, enter 2 for rock, enter 3 for paper:  ")
    player=int(player)
    bot_choice=random.choice([1,2,3])
    print("bot choice:", bot_choice)
    
    if player==bot_choice:
        print("Draw!")
    elif (player==1 and bot_choice==2) or (player==2 and bot_choice==3) or (player==3 and bot_choice==1):
        print("Lose!")
    elif (player==1 and bot_choice==3) or (player==2 and bot_choice==1) or (player ==3 and bot_choice==2):
        print("Win!")
    else:
        print("Invalid!")


def S():
    while True:
        choice=Menu()
        if choice=="1":
            print("Let's get started!")
            Rockpaperscissor()
        elif choice=="2":
            print("Quit")
            break
S()


