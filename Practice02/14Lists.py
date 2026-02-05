#BASIC EXAMPLES WITH LISTS

#1 Creation of list
mylist = ["Tair", "Timur", "Islam", "Nicola", "Napoleon"]
print(mylist)

#2 List indexation
lst = [1, 2, 3, 4, 5, 6, 7]
print(lst[0], lst[1], lst[2], lst[3])

#3 Allow duplicate for creation
lst_dublicates = [1, 1, 1, 1, 1, 1, 1, 1, 1]
print(lst)

#4 Another way to create list
lst2 = list("string")
print(lst2)

#5 List slices
print(lst2[2:5])


#ACCESS LIST ITEMS EXAMPLES

#1 List indexation
countries = ["Kazakhstan", "USA", "Britany", "Kanada", "Bangladesh", "Thailand", "UAE", "Brazil", "Australia"]
print(countries[0])
print(countries[5])
print(countries[-1])

#2 List Slices
print(countries[1:])
print(countries[1:6:2])
print(countries[::5])
print(countries[-1:0:-2])
print(countries[-1:-7:-3])
print(countries[::])

#3 Check if object in list
item = input()
if item in countries:
    print(f"{item} is a country")
else:
    print(f"{item} is not a country")



#CHANGING LIST ITEMS EXAMPLES

#1 Using indexes
universities = ["KBTU", "ALMAU", "ALFARABI", "ITU",]
universities[-1] = "SATPAEV UNIVERSITY"
universities[-2] = "SDU"

#2 Using slices
universities[1:2] = ["GARVARD", "OXFORD"]
print(universities)