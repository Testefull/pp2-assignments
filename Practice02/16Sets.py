#BASIC SETS EXAMPLES

#1 Set initialization
first = {1, True, "Yes", 0, 9.22}
second = set([1, 2, 3, 4, 5, 6, "TRue", True])
third = set(("yes", "Yes", "No", "no", "no"))
print(first, second, third)

#2 Length of the set
print(len(first))
print(len(second))
print(len(third))

#3 True and 1/ False and 0 are the same values in sets
nd1 = {True, 1}
nd2 = {False, 0}
print(nd1, nd2)

#4 Dublicates are not allowed in sets
n1 = {1, 1, 1, 1, 1, 1, 1, 1, 1, 2}
print(n1)


#ACCESS SET ITEMS EXAMPLES

#1 Using For Loops
names = {"Tair", "Alinur", "Aybar"}
digits = {1, 2, 3, 4, 5, 6, 6, 7}

for name in names:
    print(name)

for num in digits:
    print(num)

#2 Using membership operator
print(1 in digits)
print(10 in digits)
print("Alina" in names)
print(123 in digits)
print(123 not in digits)


#UPDATIN LIST ITEMS EXAMPLE

#1 Using add() method
great_inventors = {"Nicola Tesla", "Ilon Mask", "Tony Stark"}
great_inventors.add("Albert Einstein")
print(great_inventors)

#2 Using update() method
cars = {"Toyota", "Ferrari", "Lexus", "Lamborhini"}
cars.update(("Lada", "UAZ", "Chevrolet"))
cars.update(["Dewoo Matiz", "Mitsubishi", "Nissan"])
print(cars)


#DELETING ELEMENTS EXAMPLES

#1 Using remove() method
values = {"s1", "s2", "s3", "s4", "s5", "s6", "s7"}
values.remove("s1")
values.remove("s2")
values.remove("s3")
# values.remove("s8") - will raise an ERROR

#2 Using discard() method
values1 = {"n1", "n2", "n3", "n4", "n5", "n6", "n7", "n8", "n9", "n10"}
values1.discard("n1")
values.discard("n22") #No error
values.discard("n123") #No error

#3 Using pop() method
values1.pop()
values1.pop()


#4 Using clear() method
values1.clear()

#5 Complete deletion of the set
del values1


#LOOPING THROUGH SETS EXAMPLES

#1
phones = {"Iphone", "Samsung", "Xiaomi", "Poco", "Vivo"}
for phone in phones:
    print(f"{phone} is the best phone ever")

#2
avengers = {"Thor", "Iron Man", "Capitan America", "Hulk"}
villians = {"Zeus", "Loki", "Red Skull", "Red Hulk"}

for hero in avengers:
    for bad in villians:
        print(f"{hero} VS {bad}")
    print("\n")

#3
games = ["Battlefield 4", "Doom The Dark Ages", "Narutto Ultimate Ninja Storm 4", "Doom 64", "Doom 64", "Battlefield 4",
         "Battlefield 4", "Battlefield 4", "Battlefield 4", "Battlefield 4"]
g_set = set(games)

for game in g_set:
    print(game)

#4 
numers = [11, 11, 11, 11, 11, 11, 10, 10 ,10, 10, 10, 21, 12, 12, 12, 12, 21, 21, 21, 21, 21, 21, 21]
s_num = set(numers)
summ = 0

for num in numers:
    summ += num
print(summ)

#5
predators = set()
predators.add("wolf")
predators.add("tiger")
predators.add("lion")
predators.add("shark")

for a in predators:
    if a == "rabbit":
        print("rabbit is not a predator")


#SETS OPERATIONS EXAMPLES

#1 Using union() method and operator
fruits = {"apple", "pineapple", "mango", "banana"}
food = {"potato", "apple", "rice", "meat", "banana"}
iphones = {"Iphone X", "Iphone 11", "Iphone 12", "Iphone 13"}
print(fruits | food)
print(fruits.union(food))
print(fruits | food | iphones)
print(food.union(fruits, iphones))

#2 Using update() method
fruits.update(food)
food.update(fruits)
print(fruits)
print(food)

#3 Using intersection() method and operator
set1 = {True, "Michail", "yes", 777, "Alexander the Great"}
set2 = {1, "Askar", "no", 999, "Alexander the Great"}
print(set1.intersection(set2))
print(set1 & set2)

#4 Using itersection_update() method:
set3 = {"Yes", "no", 123, 777, 999}
set4 = {"Yes", 123, 999}
set3.intersection_update(set4)
print(set3)

#5 Using difference() and difference_update() methods
car1 = {"MClaren", "Toyota", "Lexus", "Chevrolet", "Ferrari"}
car2 = {"Lexus", "Ferrari", "Lamborgini", "Nissan", "Bently", "Rols Roys"}
print(car1.difference(car2))
print(car1 - car2)

car1.difference_update(car2)
print(car1)

#6 Using symmetric_difference() and symmetric_difference_update() methods
scientists = {"Albert Einstein", "Isaac Newton", "Marie Curie", "Galileo Galilei"}
artists = {"Leonardo da Vinci", "Pablo Picasso", "Marie Curie", "Michelangelo"}
leaders = {"Nelson Mandela", "Winston Churchill", "Leonardo da Vinci", "Isaac Newton"}

print(scientists.symmetric_difference(artists))
print(scientists ^ artists)
print(scientists ^ artists ^ leaders)

scientists.symmetric_difference_update(artists, leaders)
print(scientists)


#FROZEN SET EXAMPLES
set_a = frozenset({"Albert Einstein", "Isaac Newton", "Marie Curie", "Nikola Tesla"})
set_b = frozenset({"Marie Curie", "Leonardo da Vinci", "Nikola Tesla", "Galileo Galilei"})
set_c = frozenset({"Isaac Newton", "Galileo Galilei", "Ada Lovelace", "Nikola Tesla"})

#1 All basic set operations
print(set_a | set_b)
print(set_a & set_b)
print(set_a - set_b)
print(set_a ^ set_b)
print(set_a | set_b | set_c)
print(set_a & set_b & set_c)
print(set_a ^ set_b ^ set_c)

#2 Using isdisjoint() method
print(set_a.isdisjoint(set_b))
print(set_a.isdisjoint(set_c))
print(set_b.isdisjoint(set_c))

#3 Using issubset() and issuperset()
print(set_c.issubset(set_a))
print(set_c.issubset(set_b))
print(set_c.issuperset(set_a))
print(set_c.issubset(set_b))


#SET METHODS EXAMPLES
cars_1 = {"Toyota", "BMW", "Audi", "Tesla", "Ford"}
cars_2 = {"Tesla", "Ford", "Mercedes", "Honda", "BMW"}

print(cars_1.union(cars_2))
print(cars_1.intersection(cars_2))
print(cars_1.difference(cars_2))
print(cars_1.symmetric_difference(cars_2))
print(cars_1.issubset(cars_2))
print(cars_1.issuperset(cars_2))
cars_1.add("KIA")

copy_set = cars_2.copy()
print(cars_2)

empty_set = cars_1.clear()
print(empty_set)