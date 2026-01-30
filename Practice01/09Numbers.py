#Examples with numbers

#1 Type Conversion
x = 10
y = 20.5
z = 15j

print(complex(x), complex(y), complex(z))

#2 Random number generation
import random

rand_num = random.randint(1, 10)
rand_num2 = random.randrange(1, 10, step=2)

print(rand_num, rand_num2)

#3 Main Numeric datatypes
a = 11
b = 12.3
c = 77 + 10j
print(type(a), type(b), type(c))

#4 Ariphmetic operations
power = 2 ** 3
division = 10 / 5

n1 = 2 + 1j
n2 = 11 + 10j
summ = n1 + n2

print(power, division, summ)

#5 Negative numbers
n3 = -9.99
n4 = -7.77
print(abs(n3), round(n3))
print(abs(n4), round(n4))


