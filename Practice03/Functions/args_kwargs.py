# 1 Using *args in function
def count_points(*points):
    summ = 0
    for num in points:
        summ += num
    
    if summ > 100:
        return 100
    
    return summ

print(count_points(60, 20, 20)) 
print(count_points(7, 25, 39))

#2 Unpacking arguments for functions
my_marks = [1, 1, 1, 20, 1, 1, 1, 1, 20, 1, 1, 1, 40]
print(count_points(*my_marks))

#3 Using **kwargs in function + unpacking arguments
def get_info(**kwargs):
    print(f"Name: {kwargs['name']}")
    print(f"City: {kwargs['city']}")
    print(f"University: {kwargs['university']}")

data = {'name': 'Tair', 'city': 'Almaty', 'university': 'KBTU'}
get_info(**data)
get_info(name='Sergey', city='Guangzhou', university='IDK')

#4 Combination of *args and **kwargs
def mortal_kombat(*fighters, **abilities):
    for name in fighters:
        print(f"{name} - {abilities[name]}")

abilities = {'Sub-zero': 'Ice Ball', 'Scorpion': 'Fire Ball', 'Sonya': 'Death Kiss'}
mortal_kombat('Sub-zero', 'Scorpion', 'Sonya', **abilities)