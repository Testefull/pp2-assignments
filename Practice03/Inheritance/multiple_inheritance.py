#1 
class Ninja:
    def attack(self):
        return "Throws shuriken."


class Sage:
    def sage_mode(self):
        return "Activates Sage Mode!"


class Naruto(Ninja, Sage):
    pass


naruto = Naruto()
print(naruto.attack())
print(naruto.sage_mode())

#2
class Pirate:
    def sail(self):
        return "Sailing the Grand Line."


class Swordsman:
    def sword_attack(self):
        return "Performs a powerful sword slash!"


class Zoro(Pirate, Swordsman):
    pass


zoro = Zoro()
print(zoro.sail())
print(zoro.sword_attack())

#3
class Human:
    def eat(self):
        return "Eating food."


class Hero:
    def fight(self):
        return "Fighting monsters!"


class Finn(Human, Hero):
    def introduce(self):
        return "I'm Finn the Human!"


finn = Finn()
print(finn.introduce())
print(finn.eat())
print(finn.fight())

#4
class Genius:
    def invent(self):
        return "Creates new technology."


class Billionaire:
    def invest(self):
        return "Invests millions of dollars."


class Hero:
    def save_world(self):
        return "Saves the world."


class IronMan(Genius, Billionaire, Hero):
    pass


tony = IronMan()
print(tony.invent())
print(tony.invest())
print(tony.save_world())

