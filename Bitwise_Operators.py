#Bitwise operators (binary operators)

"""
&  and
| or
^ XOR
~ NOT
<< Left Shift
>> Right Shift
"""

a = 5
b = 4

print (a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a<<3) # a * 2^3 = 5*8=40
print(a>>2) # a / 2^2 = 54 = 1

#Covert decimal to binary
n = int(input("Enter a number: "))

def dec_to_bin_math(n):
    if n == 0:
        return "0"

    binary_string = ""
    while n > 0:
        remainder = n % 2
        # Add the remainder to the front of the string
        binary_string = str(remainder) + binary_string
        n = n // 2  # Integer division
    return binary_string

print(dec_to_bin_math(n))

def dec_to_bin_math(n):
    return f"{n:b}"
print(dec_to_bin_math(n))

print(26 & 23)
print(17 | 24)
print(17 ^ 24)
print(~5)
print(68<<2)
print(56>>3)
