#1 Difference between parameters and arguments
def cartoon(name): # "name" is a parameter
    return f"My favorite cartoon is {name}"

print(cartoon("The amazing spider man")) # "The amazing spider man" is argument
print(cartoon("The amazing world of Gumball")) # "The amazing world of Gumball" is argument

#2 Number of arguments
def movies(your_name, movie_title):
    return f"My name is {your_name} and my favourite movie is {movie_title}"

print(movies("Tair", "Avatar 3"))
print(movies("Sergey")) # You can't pass only one arguement

#3 Default parameters
def student_info(name, university="KBTU"):
    return f"Student name: {name}, University: {university}"

print(student_info("Tair")) # You don't need to pass parameter "university"


#4 Positional Arguments and Keyword Arguments
def fruits(fr1, fr2, fr3):
    return f"You collected {fr1}, {fr2}, {fr3}"

print(fruits("apple", 'banana', 'kiwi')) #positional arguments
print(fruits(fr1 = 'mango', fr2 = 'papaya', fr3 = 'cherry')) #keyward arguments
print(fruits('Gomu gomu', fr2='Mera mera', fr3='Pika pika')) #mixing arguments

#5 Only Positional Arguments and Only Keyword Arguments
def func_position(dream, /):
    print(f"I am gonna be {dream}")

func_position("King of the pirates")
func_position(dream='Greatest Swords Man') #You can't use keyword arguments

def func_keywords(*,superhero):
    print(f"I am {superhero}")

func_keywords(superhero='Batman')
func_keywords("Iron man") # You can't use positional arguments