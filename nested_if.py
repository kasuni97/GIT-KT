height = int(input("Enter your height in inches: "))

if height >= 4:
    print("You can enter to the park.")
    age = int(input("Enter your age: "))
    if age <=10:
        print("No charge.")
    elif age <=18:
        print("Please pay $5.")
    else:
        print("Please pay $10.")
else:
    print("You cannot enter to the park.")
print("Have a nice day!")