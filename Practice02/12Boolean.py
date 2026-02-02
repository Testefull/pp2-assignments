#Boolean Values Examples

#1 Evaluation of expressions
print(11 == 11)
print(127 < 33 * 99)
print(11 + 23 > 99 + 63)

#2 if/else statements
x = 128

if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")

#3 Using bool() function
print(bool(0))
print(bool(0.1))
print(bool(""))
print(bool("123dshvbsd"))

#4 Using bool() functions with variables
x = 10
y = "Hello World!"
print(bool(x))
print(bool(y))

#5 Boolean values in functions
def myFunction():
    return True

if myFunction:
    print("This function returned True")
else:
    print("This function returned False")