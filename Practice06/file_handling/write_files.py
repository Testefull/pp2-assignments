#Appending data to file
with open('sample.txt', 'a') as f:
    new_users = ['Tony Stark, 55, Iron man\n', 'Monky D Luffy, 19, Pirate\n']
    f.writelines(new_users)

#Printing new data from file
with open('sample.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)
