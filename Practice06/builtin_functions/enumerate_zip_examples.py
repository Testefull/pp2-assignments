#Enumerate Aplication
students = ['Andrew', 'Dima', 'Alinur', 'Aibar', 'Elnur']

for idx, name in enumerate(students):
    print(f'Place {idx + 1}: {name}')

print('-----------------')

for idx, name in enumerate(students):
    if idx % 2 == 0:
        print(name)


#Zip Aplication
bleach = ["Ichigo", "Rukia", "Renji", "Uryu", "Orihime"]
one_piece = ["Luffy", "Zoro", "Nami", "Sanji", "Chopper"]

paired_characters = list(zip(bleach, one_piece))

for bleach, one_piece in paired_characters:
    print(f"{bleach} (Bleach) with {one_piece} (One Piece)")