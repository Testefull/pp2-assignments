#1 Difference between calss variable and object's
class MyClass:
    x = 10 # CLASS variable
    def __init__(self, val):
        self.value = val # OBJECT'S variable

#2 Deleting of properties
obj1 = MyClass(12)
print(obj1.value)
# We can delete both
del obj1.value
del obj1.x


#3 Example of global access to calss property
class Billionare:
    min_money = 1000000000
    def __init__(self, name, cur_money):
        self.name = name
        self.cur_money = cur_money
    
b1 = Billionare("Kim Gapryong", 6000000000)
b2 = Billionare("Elon Mask", 10000000000)
print(b1.min_money)
print(b2.min_money)

#4 Creatign new properties and modificating existing ones
b1.min_money = 7000000000 # changing class property
b1.cur_money = 7777777777 # changing object property

b2.kids = True #creating new object property