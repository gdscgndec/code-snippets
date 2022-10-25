# Python program to suggest the best promode to apply among the given promocodes according to the bill amount

message="""
ZOMATO 

Promocode 
TRYNEW
Get 30% discount on order of Rs. 149 and above
Max discount of Rs. 75
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ZOMATO
Get flat Rs. 100 off on order of Rs. 300 and above
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
BESTSELLER
Get 40% discount on order of Rs. 400 and above
Max discount of Rs. 200
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
print(message)

# Input the bill amount from the user
amount=int(input("Enter the amount to be paid:\u20b9"))

if amount >= 400:
    discount_BESTSELLER = 0.40*amount
    
#     Discount amount cannot exceed Rs. 200 if applying the promode BESTSELLER
    if discount_BESTSELLER > 200:
        discount_BESTSELLER = 200  
    amount_BESTSELLER = amount - discount_BESTSELLER
    
#     Discount of FLAT Rs. 100 on order of Rs 300 and above
    amount_ZOMATO = amount - 100
  
    discount_TRYNEW = 0.30 * amount
#     Discount amount cannot exceed Rs. 75 if applying the promode TRYNEW
    if discount_TRYNEW > 75:
        discount_TRYNEW = 75
    amount_TRYNEW = amount - discount_TRYNEW

    if amount_TRYNEW < amount_ZOMATO and amount_TRYNEW < amount_BESTSELLER:
        print("Apply promocode TRYNEW")
    elif amount_ZOMATO < amount_TRYNEW and amount_ZOMATO < amount_BESTSELLER:
        print("Apply promocode ZOMATO")
    else:
        print("Apply promocode BESTSELLER")

elif amount >= 300 and amount < 400:
    discount_BESTSELLER = 0
    amount_BESTSELLER = amount
    amount_ZOMATO = amount - 100
    discount_TRYNEW = 0.30 * amount
    if discount_TRYNEW > 75:
        discount_TRYNEW = 75
    amount_TRYNEW = amount - discount_TRYNEW

    if amount_TRYNEW < amount_ZOMATO and amount_TRYNEW < amount_BESTSELLER:
        print("Apply promocode TRYNEW")
    elif amount_ZOMATO < amount_TRYNEW and amount_ZOMATO < amount_BESTSELLER:
        print("Apply promocode ZOMATO")
    else:
        print("Apply promocode BESTSELLER")

elif amount >=149 and amount < 300:
    discount_BESTSELLER = 0
    amount_BESTSELLER = amount
    amount_ZOMATO = amount
    discount_TRYNEW = 0.30 * amount
    if discount_TRYNEW > 75:
        discount_TRYNEW = 75
    amount_TRYNEW = amount - discount_TRYNEW

    if amount_TRYNEW < amount_ZOMATO and amount_TRYNEW < amount_BESTSELLER:
        print("Apply promocode TRYNEW")
    elif amount_ZOMATO < amount_TRYNEW and amount_ZOMATO < amount_BESTSELLER:
        print("Apply promocode ZOMATO")
    else:
        print("Apply promocode BESTSELLER")

else:
    print("No promocode applicable")

promocode = input("Enter the promocode:").strip()

if promocode=='TRYNEW':
    if amount>=149:
        discount_TRYNEW=0.30*amount
        if discount_TRYNEW>75:
            discount_TRYNEW=75
        print("Discount on applying promode TRYNEW: \u20b9", discount_TRYNEW)
        amount_TRYNEW = amount - discount_TRYNEW
        print("Amount to be paid after successfully applying TRYNEW : \u20b9", amount_TRYNEW)
    else:
        print("Pay: \u20b9",amount)
        print("Add item worth \u20b9", 149-amount ,"or more to avail TRYNEW promocode")

elif promocode=='ZOMATO':
    if amount >= 300:
        amount_ZOMATO = amount - 100
        print("Amount to be paid after successfully applying ZOMATO: \u20b9", amount_ZOMATO)
    else:
        print("Pay: \u20b9",amount)
        print("Add item worth \u20b9", 300-amount ,"or more to avail ZOMATO promocode")

elif promocode=='BESTSELLER':
    if amount >= 400:
        discount_BESTSELLER = 0.40*amount
        if discount_BESTSELLER > 200:
            discount_BESTSELLER = 200
        print("Discount on applying promode BESTSELLER: \u20b9", discount_BESTSELLER)
        amount_BESTSELLER = amount - discount_BESTSELLER
        print("Amount to be paid after successfully applying BESTSELLER : \u20b9", amount_BESTSELLER)
    else:
        print("Pay: \u20b9",amount)
        print("Add item worth \u20b9", 400-amount ,"or more to avail BESTSELLER promocode")

else:
    print("Invalid promocode")
