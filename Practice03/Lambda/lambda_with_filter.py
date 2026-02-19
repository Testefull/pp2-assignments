#1 Filtering positive numbers
nums = [-1, 10, -3, 20, -5, -99, 44, 21]
print(list(filter(lambda x: x > 0, nums)))

#2 Filtering adults
ages = [1, 12, 89, 18, 32, 23, 14, 16, 17, 18]
print(list(filter(lambda x: x <= 18, ages)))

#3 Filtering names
names = ["Alice", "Bob", "Andrew", "Charlie"]
result = list(filter(lambda name: name.startswith("A"), names))
print(result)

#4 Filterign great people names
great_people = ["Einstein","Newton", "Marie Curie", "Nikola", "Alexander", "Napoleon"]
great_people_france = [
    "Napoleon",
    "Marie Curie",
    "Victor Hugo",
    "Louis Pasteur",
    "Joan of Arc",
    "Charles de Gaulle",
    "Claude Monet",
    "René Descartes",
    "Voltaire",
    "Alexandre Dumas"
]
print(list(filter(lambda x: x in great_people_france, great_people)))


