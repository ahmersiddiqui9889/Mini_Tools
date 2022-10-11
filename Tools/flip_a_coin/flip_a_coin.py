import random

def restart():
    userDecision = input("Would you like to play again? Y/N: ")
    if userDecision == "y" or userDecision == "Y":
        main()
    elif userDecision == "n" or userDecision == "N":
        exit()
    else:
        restart()

def main():
    value = random.randint(1,2)
    if value == 1:
        print("Heads")
    else:
        print("Tails")
    restart()
main()