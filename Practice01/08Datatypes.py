#Datatypes Examples

#1 Printing datatype
x = (1, 2, 4)
print(type(x))

#2 Type conversion
x = "1"
y = 5.5
z = "10.55"
print(int(x) + 10, y + float(z))
print(type(x), type(y), type(z))

#3 Type conversion
s = "ABCD"
s_list = list(s)
print(s_list)

#4 Type conversion
l = [1, 1, 1, 1, 2, 3, 3, 4, 4, 5, 5, 5]
print(set(l))

#5 Dictionary creation
d = {}
d["apple"] = 500
d["banana"] = 300
print(d)
