#BASIC EXAMPLES WITH DICTIONARIES

#1 Dictionary initialization
actors = {
    "Leonardo DiCaprio": "Jack Dawson",
    "Robert Downey Jr.": "Iron Man",
    "Daniel Radcliffe": "Harry Potter",
    "Johnny Depp": "Jack Sparrow",
    "Keanu Reeves": "Neo",
    "Christian Bale": "Batman (The Dark Knight Trilogy)"
}

new_dict = dict(wishlist = ["Iphone 19", "Rols Roys", 1000000], is_good_child = True, name = "Tom",)

#2 Taking length of a dictionary
print(len(actors))
print(len(new_dict))

#3 Accessing the elements
print(new_dict["is_good_child"])
print(actors["Leonardo DiCaprio"])
print(actors["Christian Bale"])

#4 type() function
print(type(actors))
print(type(new_dict))

#5 Adding new element
actors["Me"] = "KBTU student"


#ACCESSING ELEMENTS EXAMPLE
games = {
    "Minecraft": "Sandbox",
    "The Witcher 3": "RPG",
    "FIFA 24": "Sports",
    "Call of Duty": "Shooter",
    "Civilization VI": "Strategy",
    "Among Us": "Party"
}

#1 Refering to the key
print(games["Among Us"])
print(games["Call of Duty"])

#2 Using get() method
print(games.get("FIFA 24"))
print(games.get("Civilization VI"))

#3 Using keys() method
print(games.keys())

#4 Using values() method
print(games.values())

#5 Using items() method
print(games.items())

#6 Checking if the key exists
print("Minecraft" in games)

#7 Changing some element and Adding new
games["The Witcher 3"] = "The best game ever"
games["GTA V"] = "Sandbox"


#UPDATING ELEMENT EXAMPLE
historical_events = {
    "Fall of Roman Empire": 476,
    "Discovery of America": 1492,
    "French Revolution": 1789,
    "World War I": 1914,
    "Moon Landing": 1969
}

#1 Through the key
historical_events["Moon Landing"] = 2025
historical_events["Discovery of America"] = 2026
historical_events["French Revolution"] = 1991

#2 Using the update() method
historical_events.update({"Breaking of Soviet Union": 1991})
historical_events.update({"WW2": 1939})

#3 
historical_events.update({
    "Fall of the Berlin Wall": 1989,
    "Independence of India": 1947
})



#UPDATING ELEMENTS EXAMPLES
countries = {
    "France": "Paris",
    "Japan": "Tokyo",
    "Brazil": "Brasília"
}

#1 Using key
countries["Germany"] = "Berlin"
countries["Kazakhstan"] = "Astana"
countries["USA"] = "Vashington"

#2 Using update() method
countries.update({"Italy": "Rome"})
countries.update({
    "Canada": "Ottawa",
    "Spain": "Madrid"
})


# REMOVING ELEMENTS EXAMPLES

#1 Using pop() method
countries.pop("USA")
countries.pop("Italy")
print(countries)

#2 Usning popitem() method
countries.popitem()
countries.popitem()
print(countries)

#3 Using a del keyword
del countries["Japan"]
del countries

#4 Using clear() method
some_dict = {1: 2, 2: 3, 3: 4, 4: 5}
some_dict.clear()
print(some_dict)


#ITERATING THROUGH DICTIONARIES
planets = {
    "Mercury": 0,
    "Venus": 0,
    "Earth": 1,
    "Mars": 2,
    "Jupiter": 95
}


#1 Iterating through keys
for key in planets:
    print(key)

print("------------")

for key in planets:
    print(planets[key])

#2 Iteration through values()
for val in planets.values():
    print(val)

#3 Iterating throught keys()
for key in planets.keys():
    print(key)

#4 Iteratig through items()
for item in planets.items():
    print(item[0], item[1])

#5
for key, val in planets.items():
    print(key, val)


#COPYING EXAMPLES

#Using copy() method
cp_1 = planets.copy()
cp_2 = games.copy()
cp_3 = historical_events.copy()

#Using dict() function
cp_4 = dict(planets)
cp_5 = dict(games)
cp_6 = dict(historical_events)


#NESTED DICTIONARIES EXAMPLES

#1 Creation

students_marks = {
    "Alice": {"Math": 90, "English": 85, "Science": 92},
    "Bob": {"Math": 75, "English": 80, "Science": 78},
    "Charlie": {"Math": 88, "English": 90, "Science": 85}
}

company = {
    "HR": {"Alice": {"age": 30, "salary": 50000}, "Bob": {"age": 28, "salary": 48000}},
    "IT": {"Charlie": {"age": 35, "salary": 70000}, "David": {"age": 32, "salary": 68000}}
}

weather_data = {
    "New York": {"temperature": {"morning": 5, "afternoon": 12, "evening": 8}, "humidity": 60},
    "London": {"temperature": {"morning": 7, "afternoon": 14, "evening": 10}, "humidity": 70},
    "Tokyo": {"temperature": {"morning": 10, "afternoon": 18, "evening": 15}, "humidity": 65}
}

#2 Iterating throught nested dictionary
for city in weather_data:
    print(f"Data about {city}")
    for tm in weather_data[city]:
        print(tm)
print("---------------")

for student in students_marks:
    print(f"Marks of {student}")
    for sub in students_marks[student]:
        print(f"{sub}: {students_marks[student][sub]}")
    print("---------------")


#DICTIONARY METHODS EXAMPLES
my_dict = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "Data Analysis", "Machine Learning"],
    "education": {
        "undergrad": "Computer Science",
        "grad": "Data Science"
    }
}

print(my_dict.values())
print(my_dict.items())
print(my_dict.keys())
print(my_dict.get("education"))
print(my_dict.get("education").pop("grad"))
my_dict.get("education").update({"grad": "Hogwarts"})
print(my_dict)
my_dict.setdefault("gender", "Female")
