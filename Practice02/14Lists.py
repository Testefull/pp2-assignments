#BASIC EXAMPLES WITH LISTS

#1 Creation of list
mylist = ["Tair", "Timur", "Islam", "Nicola", "Napoleon"]
print(mylist)

#2 List indexation
lst = [1, 2, 3, 4, 5, 6, 7]
print(lst[0], lst[1], lst[2], lst[3])

#3 Allow duplicate for creation
lst_dublicates = [1, 1, 1, 1, 1, 1, 1, 1, 1]
print(lst)

#4 Another way to create list
lst2 = list("string")
print(lst2)

#5 List slices
print(lst2[2:5])


#ACCESS LIST ITEMS EXAMPLES

#1 List indexation
countries = ["Kazakhstan", "USA", "Britany", "Kanada", "Bangladesh", "Thailand", "UAE", "Brazil", "Australia"]
print(countries[0])
print(countries[5])
print(countries[-1])

#2 List Slices
print(countries[1:])
print(countries[1:6:2])
print(countries[::5])
print(countries[-1:0:-2])
print(countries[-1:-7:-3])
print(countries[::])

#3 Check if object in list
item = input()
if item in countries:
    print(f"{item} is a country")
else:
    print(f"{item} is not a country")



#CHANGING LIST ITEMS EXAMPLES

#1 Using indexes
universities = ["KBTU", "ALMAU", "ALFARABI", "ITU",]
universities[-1] = "SATPAEV UNIVERSITY"
universities[-2] = "SDU"

#2 Using slices
universities[1:2] = ["GARVARD", "OXFORD"]
print(universities)
universities[3:4] = ["HOGWARTS", "YALE"]
print(universities)

#3 Using the insert method
universities.insert(-3, "MARINE ACADEMY")
universities.insert(1, "AVANGER'S ACADEMY")


#ADDING LIST ITEMS EXAMPLE

#1 Using the append method
subjects = ["PP2", "Discrete Structures", "Linear Algebra", "Sociology", "History"]
subjects.append("Calculus 2")
subjects.append("Calculus 1")

#2 Using the extends method
subjects.extend(["Physics", "Chemistry", "Politilogy"])
subjects.extend({"Sub1", "Sub2", "Sub3"})
subjects.extend(("PP1", "PP3", "PP4"))
print(subjects)

#3 Using the insert method
subjects.insert(1, "Calculus 3")
subjects.insert(1, "Quantum Physics")
print(subjects)



#REMOVING ITEMS FROM LIST EXAMPLES

#1 Usin the remove() method
users = ["User1", "User2", "User3", "User4", "User5", "User6", "User7", "User8"]
users.remove("User1")
users.remove("User5")
print(users)

#2 Using pop() method
print(users.pop())
print(users.pop(0))
print(users)

#3 Using del keyword
del users[0]
del users[2]
del users #completely deletes list

#4 Using clear() method
data = [123, 4556, 456546, 97969, 94545, 78949596, 353495345, 7675845945]
data.clear()
print(data)


#LOOPING THROUGH THE LIST

#1 Using FOR loop
students = ["Tair", "Bekzat", "Mihail", "Sergey", "Danial"]
for name in students:
    print(name)

print("----------")

#2 Using FOR loop with indexes
for i in range(len(students)):
    if i % 2 == 0:
        print(students[i])

print("----------")

for i in range(len(students) - 1, -1, -1):
    print(students[i])

print("----------")

#3 Using WHILE loop
i = 0
while i < len(students):
    print(students[i])
    i += 1

print("----------")

#4 Using List Comprehension
lst = [name for name in students]
print(lst)

#LIST COMPREHENSION EXAMPLES

#1 List Comprehension with conditions / and without it
even = [x for x in range(1, 11) if x % 2 ==0]
odd = [x for x in range(1, 11) if x % 2 != 0]
all_num = [x for x in range(1, 11)]
print(even, odd)

#2 List Comprehension with iterable
data = ["Yes", "No", "No", "Yes"]
res = [string for string in data if string == "Yes"]
print(res)

#3 List Comprehension with no iterable
newlist = ["Hello World!" for i in range(7)]
figures = [i**i + i for i in range(7)]
print(newlist)
print(figures)

#4 Replacing elements with List Comprehension
original = ["Man", "Woman", "Child", "Family", "Money"]
new_lst = [x if x != "Money" else "Happiness" for x in original]
print(new_lst)


#LIST SORTING EXAMPLES

#1 Using sort() method
numbers = [1, -1, 100, 92, 0.99, 54, 23, 32, 77]
numbers.sort()
print(numbers)

#2 Using reverse sort()
numbers.sort(reverse=True)
print(numbers)

#3 Customizin the sort function
def myFunc(n):
    return abs(n - 50)

numbers.sort(key=myFunc)
print(numbers)

#4 Sort function with strings
strs = ["Frigland Shanks", "Monkey D Luffy", "Gol D Roger", "Rox D Xebec", "Trafalgar D Law", "Monkey D Garp"]
strs.sort()
print(strs)

#5 Sort function case sensitive
strs.append("oden")
strs.sort(key=str.lower)
print(strs)

#6 Reversing order
strs.reverse()
print(strs)


#COPY LISTS EXAMPLES

#1 Using copy() method
numers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
copy1 = numbers.copy()

#2 Using Slices method
copy2 = numbers[:]

#Using list() function
copy3 = list(numbers)


#JOINING OF THE LISTS EXAMPLES

#1 List Concatcatenation
lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst2 = [10, 11, 12, 13]
lst3 = ["Nami", "Robbin", "Monkey D Garp"]
print(lst1 + lst2 + lst3)

#2 append() method + loop
names = ["Oden", "Rayleight", "Imu"]
names2 = ["Korazon", "Sengoku"]

for name in names2:
    names.append(name)

#3 Using extend() method
anime = ["Bleach", "One Piece", "Naruto"]
anime.extend(["Record of Ragnarok", "Dragon Ball Z"])


# LIST METHODS EXAMPLES
characters = ["Ichigo", "Zangetsu", "Itadori", "Gojo"]
characters.append("Sasuke")
characters.insert(0, "Jiraya")
characters.extend(["Luffy", "Zoro", "Sanji"])
characters.index("Luffy")
characters.sort()
characters.reverse()
characters.clear()
