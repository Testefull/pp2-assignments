#1
class Pirate:
    def __init__(self, name, bounty):
        self.name = name
        self.bounty = bounty

class Capitain(Pirate):
    def __init__(self, name, bounty, crew_size):
        super().__init__(self, name, bounty)
        self.crew_size = crew_size

class Yonko(Capitain):
    def __init__(self, name, bounty, crew_size, territory):
        super().__init__(self, name, bounty, crew_size)
        self.territory = territory

shanks = Yonko("Red Hair Shanks", 4000000000, 1000, "New World")
print(shanks.name)
print(shanks.territory)
print(shanks.crew_size)

#2
class Shinobi:
    def __init__(self, name, village):
        self.name = name
        self.village = village
    
    def __str__(self):
        return f"{self.name} from {self.village} village"

class Hokage(Shinobi):
    def __init__(self, name, village, generation):
        super().__init__(self, name, village)
        self.generation = generation
    
    def __str__(self):
        base_info = super().__str__(self)
        return base_info + f" is the {self.generation} Hokage."
    
naruto = Hokage("Naruto Uzumaki", "Konoha", 7)
print(naruto)

#3
class Character:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Character {self.name}"

class Hero(Character):
    def __init__(self, name, weapon):
        super().__init__(self, name)
        self.weapon = weapon
    
    def __str__(self):
        return super().__str__() + f", Weapon: {self.weapon}"

class LegendaryHero(Hero):
    def __init__(self, name, weapon, title):
        super().__init__(name, weapon)
        self.title = title

    def __str__(self):
        return super().__str__() + f", Title: {self.title}"


finn = LegendaryHero("Finn", "Sword", "Hero of Ooo")
print(finn)

#4
class Superhero:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __str__(self):
        return f"{self.name} has power: {self.power}"


class Avenger(Superhero):
    def __init__(self, name, power, team):
        super().__init__(name, power)   
        self.team = team               

    def __str__(self):
        return super().__str__() + f" | Team: {self.team}"


ironman = Avenger("Iron Man", "Technology", "Avengers")
print(ironman)