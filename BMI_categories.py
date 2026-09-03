weight = float(input("Enter your weight in Kg: "))
height = float(input("Enter your height in metres: "))
BMI = weight / (height ** 2)
print('Your BMI =', round(BMI, 0))
round(BMI, 0)
if BMI < 18.5:
    print("You're underweight")
elif BMI < 25:
    print("You are normal")
elif BMI < 30:
    print("You are overweight")
else:
    print("You are obes")

