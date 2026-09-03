a = 5
b = 5
print(a is b)
print(a is not b)
print(id(a))
print(id(b)) #memory address is same as a

x = 8
y = 8.0
print(id(x))
print(id(y))

n =5
print(id(n))
n=8
print(id(n))
print( n is n)