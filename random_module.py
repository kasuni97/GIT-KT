import random
from random import randint

a= random.randint(1,5)
print(a)

b= random.randrange(1,10)
print(b)

c= random.random()
print(c)

d= random.uniform(1,5)
print(d)

l=[2,0,8,-4,5,6,-5,9]
e=random.choice(l)
print(e)

random.shuffle(l)
print(l)

