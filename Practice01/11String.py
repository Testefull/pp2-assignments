#Exapmples with strings

#1 String Concatenation
s1 = "This is"
s2 = "Ilon Mask"
print(s1 + s2)
print(s1 + ' ' + s2)

#2 Indexation and Slices of strings
s3 = "ABCDEFGHIGKLMNOP"
print(s3[0], s3[1])
print(s3[9:])
print(s3[1:10])
print(s3[3:8:2])
print(s3[-1])
print(s3[:-1:-2])

#3 Taking length of strings
s4 = "Kazakhstan"
length = len(s4)

for i in range(length):
    print(s4[i])

#4 String Methods
a = "Napoleon Bomaparte"
print(a.upper())
print(a.lower())
print(a.split())
print(a.count("a", 3, -1))
print(a.isalpha())
print(a.isdigit())
print(a.replace("a", "A"))
print(a.rfind("e"))
print(a.rjust(20, "*"))
print(a.ljust(20, "*"))

s5 = "      Alexander The Great     "
print(s5.strip())
print(s5.rstrip())

#5 Format strings
n1 = 5.29
pi = 3.14159265359
print(f"The price of the subscriprion is {n1} dollars")
print(f"The pi value approximately equeals to {pi: .2f}")

