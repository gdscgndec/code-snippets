print("This is a two variable Calculator.")
num1 = int(input("enter the first number  "))
ope = input("enter opertor + ,- , / , *     ")
num2 = int(input("enter the second number  "))
if ope == "+":
    print("output =",num1 + num2)
if ope == "-":
    print("output =",num1 - num2)
if ope == "/":
    print("output =",num1 / num2)
if ope == "*":
    print("output =",num1 * num2)
else:
    print("Error You have entered wrong OPerator boiiiiiiiiiiii")