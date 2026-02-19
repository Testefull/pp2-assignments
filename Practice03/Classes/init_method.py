#1 Basical example of using __init__() method
class Legend:
    def __init__(self, name, country):
        self.name = name
        self.country = country

l1 = Legend("Napoleon Bonaparte", "France")
l2 = Legend("Alexander the Great", "Greece")
l3 = Legend("Gengishan", "Mongolia")

print(l1.name, l1.country)
print(l2.name, l2.country)
print(l3.name, l3.country)

#2 Class implementation without __init__()
class Hero:
    pass

h1 = Hero()
h1.name = "Spider Man"
h1.team = "Avengers"

#3 Setting default parameters in __init__()
class Animal:
    def __init__(self, name, status, danger='low'):
        self.name = name
        self.status = status
        self.danger = danger

a1 = Animal('Cat', "Friendly")
a2 = Animal('Dog', "Friendly")
a3 = Animal("Shark", "Not Friednly", "high")

print(a3.name, a3.status, a3.danger)

#4 Multiple parameter in __init__()
class Country:
    def __init__(self, name, money, people, life_level):
        self.name = name
        self.money = money
        self.people = people
        self.life_level = life_level

c1 = Country("France", 9999999999, 12000000, "Middle")
c2 = Country("USA", 19191991919919, 99999999, "Middle")