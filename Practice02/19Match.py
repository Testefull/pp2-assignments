#EXAMPLES WITH MATCH

#1
command = "start"

match command:
    case "start":
        print("Starting system...")
    case "stop":
        print("Stopping system...")
    case "pause":
        print("Pausing system...")
    case _:
        print("Unknown command")

#2
point = (0, 0)

match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"X-axis at {x}")
    case (0, y):
        print(f"Y-axis at {y}")
    case (x, y):
        print(f"Point at ({x}, {y})")


#3
user = {"name": "Alice", "role": "admin"}

match user:
    case {"role": "admin"}:
        print("Admin access granted")
    case {"role": "user"}:
        print("User access granted")
    case _:
        print("No access")

#4
age = 20

match age:
    case x if x < 13:
        print("Child")
    case x if 13 <= x < 20:
        print("Teenager")
    case x if 20 <= x < 65:
        print("Adult")
    case _:
        print("Senior")

#5
score = 85

if score >= 50:
    if score >= 90:
        print("Excellent! You got an A.")
    elif score >= 75:
        print("Good job! You got a B.")
    else:
        print("You passed with a C.")
else:
    print("You failed.")


