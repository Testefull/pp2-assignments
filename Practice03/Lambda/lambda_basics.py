#1 Syntax of Lambda functions
lm_func = lambda x, y: x + y
print(lm_func(1, 3))
print(lm_func(1, 19))
print(lm_func(20, 90))

#2 Multiple arguments with lamda functions
lm_func2 = lambda x, y, z: x * (y + z)
print(lm_func2(1, 2, 3))
print(lm_func2(10, 20, 30))
print(lm_func2(7, 8, 9))

#3 Different datatypes and conditions in lamda functions
is_younko_check = lambda bounty: bounty > 1000000000
if is_younko_check(3000000000):
    print("He is Yonko")
else:
    print("He is not yonko")

#4 Using lamda functions in another functions
def power_func(num):
    return lambda a: a ** num

square = power_func(2)
cubic = power_func(3)
print(square(15))
print(square(17))
