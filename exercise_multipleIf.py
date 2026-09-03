height = float(input("Please enter your height in feet: "))
bill = 0
if height >= 5:
    print("You can ride")
    age = int(input("Please enter your age: "))
    if age < 12:
        print("Please pay $5")
        bill = 5
    elif age < 18:
        print("Please pay $7")
        bill = 7
    else:
        print("Please pay $10")
        bill = 10
    want_photo = input("Please enter whether you want photo? (y/n): ")
    if want_photo == "y"or want_photo == "Y":
        bill = bill + 2
        print(f"You total bill is {bill}")
else:
    print("You can not ride")
print("Thank you! \nHave a nice day!")

