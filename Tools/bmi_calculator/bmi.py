Height = float(input("Enter height in centimeters: "))
Weight = float(input("Enter weight in Kg: "))
Height = Height/100
BMI = Weight/(Height*Height)
ind = "Your BMI indicates:"
print("Your Body Mass Index is: ", BMI)
if(BMI>0):
        if(BMI<=16):
		print(ind, "Severely underweight")
	elif(BMI<=18.5):
		print(ind, "Underweight")
	elif(BMI<=25):
		print(ind, "Healthy")
	elif(BMI<=30):
		print(ind, "Overweight")
	else: print(ind, "Severely overweight")
else:("Enter valid details")
input()
