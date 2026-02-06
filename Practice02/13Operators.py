#ARIPHMETIC OPERATORS EXAMPLES

#1 Summing, Multiplication, Division, Substraction
a = 2 * 2
b = 3 + (2 - 97 * 3)
c = a / b

print(f"a = {a}, b = {b}, c = {c}")

#2 Division by remainder
x = 4 % 2
y = 1234567890
print(f"x = {x} - remainder from devison 4 by 2")
print(f"{y % 10000} are last four figures of y")

#3 Floor Devision
num1 = 1000
print(f"{num1 / 3} - Simple division can return float value")
print(f"{num1 // 3} - Floor divison will always return integer, because it rounds down the values" )

#4 Power
print(2 ** 3)
print(3 ** 2)
print(4 ** ((2 + 7) / 3))

#5 Even value check
if 198 % 2 == 0:
    print("The number 198 is even")
else:
    print("The number is odd")


#ASSIGNMENT OPERATORS EXAMPLES

#1 Variable Assignment
a = 100
b = "one hundred"
c = [1, 2, 3, 4, 5]
x, y, z = 1, 2, 3

#2 Warlus Operator
if count := len(c):
    print(f"List C conains {count} values")

#3 Assignment + Ariphmetic
n = 9999
n += 1
n -= 1
n /= 3
n *= 3
n %= 3
print(n, end="\n")
print(f"Remainder of division by 3: {n}")

#4 Bitwise + Assignment
num1, num2, num3, num4 = 2, 2, 2, 2
num1 &= 3
num2 |= 3
num3 ^= 3
num4 >>= 3 
print(f"The result of logical AND: {num1}")
print(f"The result of logical OR: {num2}")
print(f"The result of logical NOT: {num3}")
print(f"The result of bit shifting to the right: {num4}")

#5 Assignment
num5, num6, num7 = [1, 2, "Banana"]


#COMPARISON OPERATORS EXAMPLES

#1 Basic operators
x = 77
y = 99
print(x == y)
print(y > x)
print(x < y)
print(x >= y)
print(x <= y)
print(x != y)


#2 Chaining Comparison operators
print(100 >= 99 and 100 <= 1000)
print(1000 < 2000 and 1000 > 100)
print((1 + 1) > (1 - 1) or (88 * 8) > (77 * 7))

#3 Usin in if/else statements
x = 137
if x % 2 == 1:
    print("ODD")
else:
    print("EVEN")

#4 Applying is the len
print(len("Hello World!") < len("Pyhthon is the best programming language"))

#5 Just example
print(round(2.99) < 3.0)


#LOGICAL OPERATORS EXAMPLES

#1 AND
print(f"True and True: {1 and 1}") 
print(f"False and True: {0 and 1}")
print(f"True and False: {1 and 0}")
print(f"False and False{0 and 0}")

#2 OR
print(f"True and True: {1 or 1}") 
print(f"False and True: {0 or 1}")
print(f"True and False: {1 or 0}")
print(f"False and False{0 or 0}")

#3 NOT
print(f"Not True is False: {not 1}")
print(f"Not False is True: {not 0}")

#4 Interval Creation
x = 777
print(x >= 600 and x <= 800)

#5 Just example
print(not(x >= 600 and x <= 800))


#IDENTITY OPERATORS

#1 Pointing at the same object
a = {1, 3, 4}
b = a
c = {1, 3, 4}

print(a is b)
print(b is a)
print(c is a)
print(c == a)

#2 Using is not
print(c is not a)

#3 Just example
string = "aaaaaaa"
same_obj = string
copy_string = string[:]
print(string is same_obj)
print(string is copy_string)

#4 Just example
print(1 is 1)

#5 Just example
print(2 is 2 * 1)


#MEMBERSHIP OPERATORS

#1 With lists
fruits = ["banana", "apple", "orange"]
print("banana" in fruits)
print("cucuber" not in fruits)

#2 With strings
name = "Tesla Nicola"
name_short = "Tesla N"
print('Tesla' in name)
print("Nicola" in name)
print("Nicola" in name_short)

#3 With Tuples
data = ("Man", "Human", "Monkey")
print("Man" in data)
print("D Luffy" not in data)

#4 With Dictionaries
marks = {
    "Tair": 100,
    "Sergey": 99,
    "Timur": 77
}

print("Tair" in marks)
print(100 in marks)

#5 With Sets
unique = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(1 in unique)
print(100 not in unique)


#BITWISE OPERATORS

#1 BITWISE AND
print(77 & 8)

#2 BITWISE OR
print(77 | 8)

#3 XOR
print(77 ^ 8)

#4 BITWISE NOT
print(~77)

#5 RIGHT / LEFT HSIFT
print(77 >> 2)
print(77 << 2)


# OPERATOR PRECENDENSE EXAPLES

# 1 Parethesis are the most important
print((2 + 4) * 8)

#2 Exponentiantion - top 2
print((2 + 7)**2 * 9)

#3 Ariphmetic operators - top 3
print(1 + 2 * 2 + 3 % 6 - 100 / 5)

#4 Bitwise operators - top 4
print(100 >> 2 & 100 << 2)

#5 Comparison operators - top 5 / Logical operators - top 6
print(1 >= 3  and 1 <= 5)