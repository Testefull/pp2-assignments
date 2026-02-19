#1 Inverting numbers with map function
nums1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(map(lambda x: x * (-1), nums1)))
print(list(map(lambda x: x * (-1), nums2)))


#2 Changing case of text
names = ['luffy', 'thor', 'naruto']
print(list(map(lambda t: t.upper(), names)))

#3 Taking the length of words
people = ["Napoleon", "Gengishan", "Stalin", "Ichigo"]
length = list(map(lambda x: len(x), people))
print(length)

#4 Cubpic values of numbers
numbers = [10, 11, 12, 13, 14, 15, 16]
print(list(map(lambda x: x ** 3, numbers )))

#5 Trancefring Celcius and Farenheit
celsius = [0, 20, 30, 100]
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
print(fahrenheit)