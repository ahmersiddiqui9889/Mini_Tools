import random

def generate_random_number(lowerlimit, upperlimit):
    # generate a random number between lowerlimit and upperlimit
    randomnum = random.randint(lowerlimit, upperlimit)
    return randomnum

def main():
    # get lowerlimit
    lowerlimit = int(input("Enter the lower limit: "))
    # get upperlimit
    upperlimit = int(input("Enter the upper limit: "))

    randomNum = generate_random_number(lowerlimit, upperlimit)
    print("The random number is: ", randomNum)

if __name__ == "__main__":
    main()