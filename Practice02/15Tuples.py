#BASIC TUPLE EXAMPLES

#1 Initialization of tuple
first = ("Yes", True, 0, False, 123, [1, 2, 3], 9.99)
second = tuple([1, 2, 3, 4, 5, 6, 7])
third = (1, )
not_tuple = (1)
print(type(third) == type(not_tuple))

#2 Indexation of tuple
print(first[1])
print(second[4])

#3 Taking the length of the tuple
print(len(first))


# ACCESS TUPLE ITEMS EXAMPLES

#1 Indexation / Negative indexation
tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tp[0])
print(tp[1:10])
print(tp[1:6:2])
print(tp[-1])
print(tp[-1:-9:-1])
print(tp[10:1:-1])
print(tp[1:])
print(tp[:10])

#2 Using membership operators
print(10 in tp)
print(1 in tp)


#UPDATING TUPLES EXAMPLES

#1 Adding elements
lst = list(tp)
lst.append(11)
lst.extend([12, 13, 14, 15, 16, 17])
tp = tuple(lst)

#2 Deleting of elements
lst = list(tp)
lst.remove(1)
lst.pop()
tp = tuple(lst)

#Deleting of entire tuple
del tp


#UNPACKING TUPLES EXAMPLES

#1 Unpacking to multiple variables
colors = ("red", "blue", "green")
great_people = ("Napoleon Bonaparte", "Alexander the Great", "Tomiris Patshasy")
c1, c2, c3 = colors
p1, p2, p3 = great_people
print(c1, c2, c3)
print(p1, p2, p3)

#2 Unpacking using the Astrics *
anime_heroes = ("Naruto", "Gin", "Zack Lee", "Daniel Park", "Gun Park")
naruto, bleach, *lookism = anime_heroes
print(naruto)
print(bleach)
print(lookism)

cities = ("Astana", "Almaty", "Shymkent", "New York", "Stanbul")
*kz, usa, tr = cities
print(kz)
print(usa)
print(tr)


#LOOP TUPLES EXAMPLES

#1 Using FOR loop
values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
summ = 0
for num in values:
    summ += num

print(num)

#2 Usin FOR loop with indexes
for i in range(len(values)):
    print(values[i])

#3 Using WHILE loop with indexes
j = 0
while j < len(values):
    print(values[j])
    j += 1

#4 Just an example
names = ("Tair", "Aybar", "Alinur")
universities = ("KBTU", "Stapaev", "KazNAU")

for i in range(len(names)):
    print(f"{names[i]} is the student of {universities[i]}")


#JOINING TUPLES EXAMPLES

#1 Tuple Concatenation
tp1 = (1, 2, 3)
tp2 = (4, 5, 6)
tp3 = tp1 + tp2
print(tp3)

authors_rus = ("Pushkin", "Dostievsky", "Tolstoy")
authors_en = ("Kristi", "Shakespeare")
great_authors = authors_rus + authors_en
print(great_authors)

#2 Tuple Multiplication
vegetables = ("cucumber", "tomato", "potato", "carrot")
digits = (7, )
print(vegetables * 3)
print(digits * 7)


#TUPLE METHODS EXAMPLES

#1 count() 
tp = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
print(f"There is {tp.count()} ones in this tuple")

#2 index()
tp_unique = (1, 9 ,0 ,3, 349)
print(f"Number 349 is in {tp.index(349)} index")






