#1 Basic Example
class Shinobi:
    def attack(self): #Parental method
        return "Shinobi throws a kunai."


class Genin(Shinobi):
    def attack(self): #Overriding method
        return "Genin uses Shadow Clone Jutsu!"


ninja = Genin()
print(ninja.attack())


#2 Another example
class Leader:
    def rule_style(self):
        return "Leads with democracy."


class Dictator(Leader):
    def rule_style(self):   # overriding
        return "Rules with absolute power."


person = Dictator()
print(person.rule_style())


#3 Another example
class Hero:
    def aim(self):
        return "Save the world!"

class Villian(Hero):
    def aim(self):
        return "Destroy the world!"

#4 Another example
class Pirate:
    def say_smth(self):
        return "I will conquer the see"
    
class PirateKing(Pirate):
    def say_smth(self):
        return "I will be the most free person in the world"