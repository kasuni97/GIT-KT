pizza = input("Hi!! Do you want to order a pizza (y/n):")
if pizza == "y" or pizza == "Y":
    size = input("Please enter preferred pizza size (Small / Medium/ Large: ")
    bill = 0
    if size == "Small " or size == "small" or size == "S" or size == "s":
        bill = 100
        print("Small pizza price is Rs. 100")
    elif size == "Medium " or size == "medium" or size == "M" or size == "m":
        bill = 200
        print("Medium pizza price is Rs. 200")
    else:
        bill = 300
        print("Large pizza price is pay Rs. 300")
    add_pepperoni = input("Do you want to add pepperoni (y/n):")
    if add_pepperoni == "y" or add_pepperoni == "Y" :
        if size == "Small " or size == "small" or size == "S" or size == "s":
            bill = bill + 30
        else:
            bill = bill + 50
    add_extra_cheese = input("Do you want to add extra cheese (y/n):")
    if add_extra_cheese == "y" or add_extra_cheese == "Y":
        bill = bill + 20
        print(f"You total bill is {bill}")
    else:
        print(f"You total bill is {bill}")
    print("Thank you for your order! \n Enjoy your pizza!")
else:
    print("Thank you for your time!")

