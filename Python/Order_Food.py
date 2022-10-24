# Python program where user can select the dishes they want from the Mc Donald's Menu and its quantity and add it to the cart and at the end the total bill amount will be displayed to the user

# Menu
Mc_Donalds_Menu = [
    {
        "Name" : "McAloo Tikki Burger",
        "Price" : 52,
        "Quantity" : 0
    },
    {
        "Name" : "Veg Maharaja Mac",
        "Price" : 204,
        "Quantity" : 0
    },
    {
        "Name" : "McChicken",
        "Price" : 127,
        "Quantity" : 0
    },
    {
        "Name" : "Chicken McNuggets 6pc",
        "Price" : 153,
        "Quantity" : 0
    },
    {
        "Name" : "Butter Paneer Grilled",
        "Price" : 109,
        "Quantity" : 0
    },
    {
        "Name" : "Fries",
        "Price" : 114,
        "Quantity" : 0
    },
    {
        "Name" : "Coke",
        "Price" : 94,
        "Quantity" : 0
    },
    {
        "Name" : "Cold Coffee",
        "Price" : 98,
        "Quantity" : 0
    },
    {
        "Name" : "Chocolate Brownie Sundae",
        "Price" : 109,
        "Quantity" : 0
    },
    {
        "Name" : "Pizza McPuff",
        "Price" : 44,
        "Quantity" : 0
    }
]
print(Mc_Donalds_Menu)

#  A function named shopping_cart where all the dishes will be added
def shopping_cart():

    cart =[]

    total_amount = 0
    total_dishes = 0
    
#     Taking the dishes input from user until they want to add the items to the cart
    choice = "Yes"
    while choice == "Yes":
        dish_name = input("Enter dish name: ")

        for index in range(len(Mc_Donalds_Menu)):
            if Mc_Donalds_Menu[index]["Name"] == dish_name:
                quantity = int(input("Enter the quantity for "+dish_name+" :"))
                Mc_Donalds_Menu[index]["Quantity"] = quantity
                total_dishes += quantity
                total_amount += quantity * Mc_Donalds_Menu[index]["Price"]
                cart.append(Mc_Donalds_Menu[index])
                break
        
        choice = input("Do you wish to continue(Yes or No): ")
        
    print("CART [", len(cart) ,"]") 
    print(cart)
    print("Total Dishes:", total_dishes)
    print("Please Pay: \u20b9", total_amount)

    return total_amount

result = shopping_cart()
