# BMI Calculator using python (BMI --> BODY MASS INDEX)
# Body mass index (BMI) is a measure of body fat based on height and weight that applies to adult men and women.
# According to BMI:
# a person is said to be UNDERWEIGHT if he/she falls in the BMI range 0-18.4
# a person is said to have NORMAL WEIGHT if he/she falls in the BMI range 18.5 - 24.9
# a person is said to be OVERWEIGHT if he/she falls in the BMI range 25 - 29.9
# a person is said to be OBESE if he/she falls in the BMI range >= 30

# Enter your respective weight in Kilograms and height in meters.

Weight = float(input("Enter your weight in Kg(s):-  "))
Height = float(input("Enter your height in m(s):- "))

# formula to calculate BMI (Kg/m^2)
BMI_cal = Weight/(Height*Height)
print("your Body Mass Index is: ", BMI_cal)

if BMI_cal > 0:

	if BMI_cal <= 18.4:
		print("you are Underweight")

	elif BMI_cal <= 24.9:
		print("you are Healthy")

	elif BMI_cal <= 29.9:
		print("you are Overweight")

	elif BMI_cal >= 30:
		print("you are Obese.")

else:
	print("Your entered details are not correct.")
	print("Kindly enter valid details to check your BMI")
