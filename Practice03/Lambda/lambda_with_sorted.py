#1 Sorting values by their absolute value only
numbers = [-10, 5, -3, 2, -1]
print(sorted(numbers, key=lambda x: abs(x)))

#2 Sorting list of tuples
characters = [("Luffy", 3000000000), ("Zoro", 1500000000), ("Sanji", 1000000000)]
print(sorted(characters, key=lambda x: x[1]))

#3 Sorting list of tuples with priority to name
print(sorted(characters, key=lambda x: x[0]))

#4 Sorting dictionary
points = {"Aidana": 85, "Tair": 92, "Charlie": 78}
result = sorted(points.items(), key=lambda item: item[1])
print(result)
