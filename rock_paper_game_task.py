import random
import os
import time
li=['rock','paper','scissor']
user_point=0
computer_points=0
print("================== welcome to the game of rock ,paper and scissor =====================")

for i in range(3):
    print(f"================== ROUND {i+1} =====================")
    user=input('enter the choice')
    computer=random.choice(li)
    print("You chose      :", user)
    print("Computer chose :", computer)
    if user==computer:
        print("It's a Tie!")

    elif (user=='rock' and computer=='scissor') or (user=='scissor' and computer=='paper') or (user=='paper' and computer=='rock'):
        user_point+=1
        print("You won this round!")

    else:
        computer_points+=1  
        print("Computer won this round!")

    print('computer_point :',computer_points)
    print('user_point:',user_point)   
    time.sleep(1)
    os.system('cls') 

    print("================== final result  =====================")

    if user_point > computer_points:
        print("Congratulations! You won the game.")
        print('computer_point :',computer_points)
        print('user_point:',user_point)   

    elif computer_points > user_point:
        print("Computer won the game.")
        print('computer_point :',computer_points)
        print('user_point:',user_point)   

    else:
        print("The game is a Tie.")
        print('computer_point :',computer_points)
        print('user_point:',user_point)   
      
       



