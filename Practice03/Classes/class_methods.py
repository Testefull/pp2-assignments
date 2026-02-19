#1 Simple example of class method
class Country:
    def __init__(self, name, money, people, life_level):
        self.name = name
        self.money = money
        self.people = people
        self.life_level = life_level
    
    def get_info(self):
        return f"Country: {self.name}; Total Economics: {self.money}; Population: {self.people}"

c2 = Country("USA", 19191991919919, 99999999, "Middle")
print(c2.get_info())

#2 Creating method with parameters
class AnimeCharacter:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def introduce(self):
        return f"My name is {self.name} and my power is {self.power}!"

    def power_up(self, amount):
        self.power += amount
        return self.power

luffy = AnimeCharacter("Luffy", 100)
print(luffy.introduce())
print(luffy.power_up(50))

#3 Example with __str__ method
class HistoricalPerson:
    def __init__(self, name, lifespan, known_for):
        self.name = name
        self.lifespan = lifespan
        self.known_for = known_for

    def __str__(self):
        return f"{self.name} ({self.lifespan}) is known for {self.known_for}."


person = HistoricalPerson("Gengis Khan", "1162–11227", "conquered the world")
print(person)

#4 Multiple class methods example
class Team:
    def __init__(self):
        self.members = []
    
    def add_member(self, person):
        if person in self.members:
            return f"{person} already in team"
        
        self.members.append(person)
        return f"{person} added to team"
    
    def delete_member(self, person):
        self.members.remove(person)
        return f"{person} removed from team"