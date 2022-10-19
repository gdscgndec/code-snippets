print("~~~~~~~~~~~~~~~~~~~The Table By Basant~~~~~~~~~~~~~~~~~~~~~")
import pprint

RESTAURANT = {"name": "The Table By Basant",
              "Reviews": 4.1,
              "Reviewed by": "113.8k customers",
              "specialisation": "north indian , pizza , burger etc.",
              "promo codes": ("GOBIG", "CRAVINGS", "ZOMATO")

              }
print(RESTAURANT)
print()
print()
print("~~~~~~~~~~~~~~~~~~~MENU~~~~~~~~~~~~~~~~~~~~~")
products = {"dal": 120,
            "cheese tomato": 130,
            "mixed vegtables": 90,
            "veg pulao": 120,
            "idli": 50,
            "vada": 70,
            "masala dosa": 110,
            "coconut chutney": 30,
            "pizza": 200,
            "burger": 80,
            "pasta": 160,
            "fries": 70,
            "shake": 100,
            "pepsi": 40,
            "gulaab jamun ": 25,
            "rasgulla": 20}

land = pprint.pformat(products)
print("\n", land)

print("~~~~~~~~~~~~~~~~~~~~LETS START BUILDING YOUR CART~~~~~~~~~~~~~~~~~~~~~~~~")
cart = []
choice = "yes"

while choice == "yes":
    product = input("Enter Product of Your Choice:")
    cart.append(products[product])
    choice = input("Would you like to add another product (yes/no)")

print("Your Cart [", len(cart), "]:")
print(cart)

total = 0

for i in cart:
    total = int(total) + int(i)

if total >= 100:
    promo_code = input("enter promo code")
    if promo_code == "GOBIG":
        discount = total * 0.4

        if discount >= 100:
            discount = 100

        taxes = 0.1 * total

        amount = total - discount + taxes
        print("required amount to be paid is:", amount, "\n please proceed for checkout!!")

    elif promo_code == "CRAVINGS":
        discount = total * 0.5

        if discount >= 100:
            discount = 100

        taxes2 = 0.1 * total

        amount = total - discount + taxes2
        print("required amount to be paid is:", amount)

    else:
        print("this code does not exists or no code has been applied")
        taxes2 = 0.1 * total
        amount = total + taxes2
    print("required amount to be paid is:", amount)
else:
    print(
        "your total amount is lower than 100 please add more items to be eligible for the application of the promo code!")
if len(cart) > 2 and total >= 100:
    print(
        "congratulations! you bought more than two items and your order is eligible for a complimentary gift of a coca cola 150 ml bottle worth RS. 20")

print("please proceed for checkout\n ORDER CONFIRMED! \n THANKS FOR SHOPPING WITH US")