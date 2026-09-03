print("Welcome to the Love Calculator")

gender = input("Are you female or male? : ")
if gender == "female" or gender == "Female" or gender == "F" or gender == "f":
    name_1 = input("Please enter your name : ")
    name_2 = input("Please enter his name : ")
else:
    name_1 = input("Please enter your name : ")
    name_2 = input("Please enter her name : ")

combine_string = name_1 + name_2
lower_case_string = combine_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

true_love_score =int( str(true)+ str(love))


if true_love_score < 10 or true_love_score > 90:
    print(f"Your score is {true_love_score}% and you go together like coke and mentos!")
elif true_love_score >= 40 and true_love_score <= 50:
    print(f"Your score is {true_love_score}% and you are alright together!")
else:
    print(f"Your score is {true_love_score}% ")