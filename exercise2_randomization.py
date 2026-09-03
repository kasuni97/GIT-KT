names = input("Enter everybody's name separated by comma : ").split(",")
print(names)
length = len(names)

import random

select_name = random.randint(0,length-1)
print(f"{names[select_name]} will pay the bill")

select_name1 = random.choice(names)
print(f"{select_name1} will pay the bill")

