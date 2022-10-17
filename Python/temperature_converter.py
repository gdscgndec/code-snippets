# Creating a temperature converter which will take input of temperature in celsius and will convert it into fahrenheit as well as kelvin.
# In this code we will represent various temperature scales:
#      Celsius --> C 
#      Fahrenheit --> F 
#      Kelvin --> K
#      Newton --> N
#      Réaumur --> Ré

# User will input the tempurature in Celsius scale

temp_in_C = float(input("Enter the tempurature in Celsius (C): "))

# Below is the formula which will convert the Celsius into Fahrenheit

temp_in_F = (temp_in_C *(9/5)) + 32

# Below is the formula which will convert the Celsius into Kelvin

temp_in_K = temp_in_C + 273.15

# Below is the formula which will convert the Celsius into Newton

temp_in_N = temp_in_C * (33/100)

# Below is the formula which will convert the Celsius into Réaumur

temp_in_Ré = temp_in_C * (4/5)

print("Celsius to Fahrenheit: ")
print("The temperature in Fahrenheit is: " , temp_in_F , "F\n")

print("Celsius to Kelvin: ")
print("The temperature in Kelvin is: " , temp_in_K , "K\n")

print("Celsius to Newton: ")
print("The temperature in Newton is: " , temp_in_N , "N\n")

print("Celsius to Réaumur: ")
print("The temperature in Réaumur is: " , temp_in_Ré , "Ré\n")





