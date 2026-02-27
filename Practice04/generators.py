#1 Square of numbers
def suquare_generators(n):
    for i in range(n):
        yield i ** 2

for num in suquare_generators(10):
    print(num, end=' ')
print()


#2 Even numbers
def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

n = int(input())

first = True
for num in even_numbers(n):
    if not first:
        print(',', end='')
    print(num, end='')
    first = False

#3 Divisible by 3 and 4
def divisible_nums(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for num in divisible_nums(100):
    print(num, end=' ')
print()


#4 Squares from a to b
a = int(input("Enter a: "))
b = int(input("Enter b: "))

def gen_squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

for num in gen_squares(a, b):
    print(num, end=' ')


#5 From n to 0
def gen_down(n):
    while n > 0:
        yield n
        n -= 1

for num in gen_down(100):
    print(num, end=' ')