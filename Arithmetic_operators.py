num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

#Arithmetic operators

sum = int(num_1) + int(num_2)
print("Summation = ",sum)
sub = int(num_1) - int(num_2)
print("Subtraction = ",sub)
mul = int(num_1) * int(num_2)
print("Multiplication = ",mul)
div = int(num_1) / int(num_2)
print("Divition = ",div)
pow = int(num_1) ** int(num_2)
print("Power = ",pow)
mod = int(num_1) % int(num_2)
print("Modulus = ",mod)

print("Flow Division = ", int(num_1) // int(num_2))

print("**************** Calculate Your BMI ********************")
weight = float(input("Enter your weight in Kg: "))
height = float(input("Enter your height in m: "))
BMI = weight / (height * height)
print("BMI = ",BMI)

