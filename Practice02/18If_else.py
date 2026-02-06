#IF STATEMENT EXAMPLES

#1 Using variables and logical operators
a = 100
b = 100
c = 50

if a == b:
    print("a and b are equal")

if c < a:
    print("c is less than a")


#2 Using of Multiple statements
country = "Japan"
if country == "Japan":
    print("You are really cool!")
    print("You must be studying in KBTU")
    print("Thats great")


#3
heroes = ["Iron Man", "Batman", "Thanos"]
if "Thanos" in heroes:
    print("Thanos is not a hero")

#4
number = 5

if number > 0:
    print("The number is positive")

#5
text = "Hello"

if text:
    print("The string is not empty")


#IF-ELIF STATEMENT EXAMPLES

#1 
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score < 70:
    print("Bro...you lost your money")

#2
temperature = 25

if temperature > 30:
    print("It's hot outside")
elif temperature > 20:
    print("The weather is nice")
elif temperature > 10:
    print("It's a bit chilly")


#3
day = "Tuesday"

if day == "Monday":
    print("Start of the work week")
elif day == "Tuesday":
    print("Second day of the week")
elif day == "Wednesday":
    print("Midweek")
elif day == "Thursday":
    print("Almost Friday")
elif day == "Friday":
    print("Last workday!")

#4
age = 16

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")

#5
temperature = 15

if temperature > 25:
    print("It's hot")
elif temperature > 15:
    print("It's warm")
elif temperature > 5:
    print("It's cool")



#IF-ELIF-ELSE Examples

#1
# Check traffic light color
traffic_light = "yellow"

if traffic_light == "red":
    print("Stop")
elif traffic_light == "yellow":
    print("Get ready to move")
else:
    print("Go")

#2
num = -7

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

#3
age = 12

if age < 5:
    print("Free ticket")
elif age <= 18:
    print("Child ticket")
else:
    print("Adult ticket")

#4
password = "abc123"

if len(password) >= 12:
    print("Strong password")
elif len(password) >= 6:
    print("Moderate password")
else:
    print("Weak password")

#5
fruit = "banana"

if fruit == "apple":
    print("Red fruit")
elif fruit == "banana":
    print("Yellow fruit")
else:
    print("Unknown color")


#SHORTHAND IF STATEMETS EXAMPLES

#1
age = 18
is_student = True
discount = 0.5 if age >= 18 and is_student else 0.2
print(f"Your discount is {discount}")

#2
num = 100
print("Number is in [100, 200]") if num >= 100 and num <= 200 else print("Number is not in this interval")

#3
score = 100
message = "Pass" if score >= 50 else "Retake"
print(message)  

#4
name = ""
status = "Empty" if not name else "Not Empty"
print(status)

#5
a = 1.99
b = 2.01
max_num = a if a > b else b
print(max_num) 


#IF-ELSE WITH LOGICAL OPERATORS EXAMPLES

#1
num = 35
if num >= 35 and num <= 50:
    print("number is in interval [35; 50]")
else:
    print("number is not in interval [35; 50]")

#2
name = "Aybar"
Kbtu_students = ["Tair", "Aybar", "Alinur", "Sergey"]
activists = ["Aybar", "Segey"]

if name in Kbtu_students and name in activists:
    print(f"{name} is KBTU student and activist")
elif name in Kbtu_students and name not in activists:
    print(f"{name} is KBTU student")
else:
    print(f"{name} is not a KBTU student")

#3
username = "user123"
password = "pass123"

if username == "user123" and password == "pass123":
    print("Login successful")
else:
    print("Invalid username or password")

#4
age = 17
has_permission = True

if age >= 18 or has_permission:
    print("Access granted")
else:
    print("Access denied")

#5
temperature = 25
raining = False
windy = True

if (temperature > 20 and not raining) or windy:
    print("Good day for outdoor activities")
else:
    print("Better stay inside")


#NESTED IF STATEMENT EXAMPLES

#1
year = 2000

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


#2
pin = 1234
balance = 5000
withdraw_amount = 1000

if pin == 1234:
    if withdraw_amount <= balance:
        balance -= withdraw_amount
        print(f"Withdrawal successful. Remaining balance: {balance}")
    else:
        print("Insufficient funds.")
else:
    print("Incorrect PIN.")

#3
age = 20
has_passport = True

if age >= 18:
    if has_passport:
        print("You are eligible to travel abroad.")
    else:
        print("You need a passport to travel.")
else:
    print("You are too young to travel alone.")


#EXAMPLES WITH PASS STATEMENTS

#1
feature_enabled = False

if feature_enabled:
    print("Feature is running!")
else:
    pass 

#2
feature_enabled = False

if feature_enabled:
    print("Feature is running!")
else:
    pass 

#3
x = 5
y = 0

if x > 0:
    if y > 0:
        print("Both positive")
    else:
        pass  
else:
    pass 

#4
user_input = ""

if user_input:
    print("Input received")
else:
    pass


#5
temperature = 25

if temperature > 30:
    print("It's hot!")
elif temperature < 10:
    print("It's cold!")
else:
    pass  











