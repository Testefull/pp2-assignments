#1 Simpliest example of inheritance
class Animal: #parent class
    mind_level = "Primal"

class Cat(Animal): #derived class
    pass

class Dog(Animal): #derived class
    pass

class Dolphin(Animal): #derived class
    pass

cat = Cat()
dog = Dog()
dolphin = Dolphin()

print(cat.mind_level, dog.mind_level, dolphin.mind_level)


#2 Another example
class Pirate:
    def __init__(self, name, bounty):
        self.name = name
        self.bounty = bounty

    def show_bounty(self):
        return f"{self.name}'s bounty is {self.bounty} berries."


class Yonko(Pirate): # Inherits all the methods from parent class
    def rule_sea(self):
        return f"{self.name} rules the New World!"


shanks = Yonko("Shanks", 4000000000)

print(shanks.show_bounty()) #parent class method
print(shanks.rule_sea()) #derived class method


#3 Another example
class Character:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says hello!"


class Hero(Character):
    def fight(self):
        return f"{self.name} fights evil!"


finn = Hero("Finn")

print(finn.speak()) # parent class method
print(finn.fight()) # derived class method

#4 Another example
class Superhero:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def use_power(self):
        return f"{self.name} uses {self.power}!"


class Avenger(Superhero):
    def assemble(self):
        return f"{self.name} joins the Avengers!"


ironman = Avenger("Iron Man", "technology")

print(ironman.use_power())
print(ironman.assemble())


