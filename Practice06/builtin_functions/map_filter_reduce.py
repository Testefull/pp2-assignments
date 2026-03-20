from functools import reduce

# Application of map
data = [1.99, 89, '190', '67', '7.99', '9.99']
new_data = list(map(float, data))
new_calculations = list(map(lambda x: round(x ** 2, 2), new_data))

print(*new_data)
print(*new_calculations)

#Application of filter
us_cities = [
    "New York",
    "Los Angeles",
    "Chicago",
    "Houston",
    "Phoenix",
    "Philadelphia",
    "San Antonio",
    "San Diego",
    "Dallas",
    "San Jose"
]

res = list(filter(lambda x: x.startswith('S'), us_cities))
print(*res)

#Application of reduce
factorial_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
final = reduce(lambda x, y: x * y, factorial_10)
print(final)