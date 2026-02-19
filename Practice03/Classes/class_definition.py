#1 Example of class creation
class Animal: #Class initialization
    pass

#Class objects
cat = Animal()
dog = Animal()
tiger = Animal()
shark = Animal()

#2 Creating class with some properties
class Pirate:
    bounty = 5000000000 #prioperty of the class

luffy = Pirate()
zoro = Pirate()
sanji = Pirate()

print(luffy.bounty)
print(zoro.bounty)
print(sanji.bounty)

#3 Deleting class objects
del luffy
del zoro
del sanji

#4 
class Human:
    age = 100

napoleon = Human()
leonardo = Human()
stalin = Human()