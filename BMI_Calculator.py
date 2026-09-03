weight = float(input('Enter weight in kg: '))
height = float(input('Enter height in m: '))

BMI = weight / (height ** 2)
print('Your BMI =', round(BMI, 0))