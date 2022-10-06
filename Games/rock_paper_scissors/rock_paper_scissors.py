# Author - DanielJ-OBrien

import random
print("Welcome to: Rock, Paper, Scissors!")

def playagain():
    userDecision = input("Would you like to play again? Y/N: ")
    if userDecision == "y" or userDecision == "Y":
        main()
    elif userDecision == "n" or userDecision == "N":
        exit()

def main():
    userChoice = input("""Type the number of your preferred move:
    1. Rock
    2. Paper
    3. Scissors
    """)
    if userChoice != "1" and userChoice != "2" and userChoice != "3":
        print("Incorrect input. Please select 1, 2, or 3.")
        main()
    AiChoice = random.randint(1,3)
    if int(userChoice) == AiChoice:
        print("Draw!")
    elif userChoice == "1":
        if AiChoice == 2:
            print("AI picked paper! You lose!")
        else:
            print("AI picked scissors! You win!")  
    elif userChoice == "2":
        if AiChoice == 3:
            print("AI picked scissors! You lose!")
        else:
            print("AI picked rock! You win!")  
    elif userChoice == "3":
        if AiChoice == 1:
            print("AI picked rock! You lose!")
        else:
            print("AI picked paper! You win!") 
    playagain() 
    
main()
