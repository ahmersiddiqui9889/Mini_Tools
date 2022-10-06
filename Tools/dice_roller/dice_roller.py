import random

def restart():
    decision = input("Go again? Y/N ")
    if decision == "Y" or decision == "y":
        main()
    else:
        exit()

def main():
    dieRolls = []
    dieCount = input("How many dice do you wish to roll? ")
    sideCount = input("How many sides should the dice have? ")
    try:
        for x in range(0, int(dieCount)):
            dieRoll = random.randint(1,int(sideCount))
            dieRolls.append(dieRoll)
    except:
        print("Invalid input detected.")
        main()
    dieRolls.sort()
    print(dieRolls)
    restart()
main()