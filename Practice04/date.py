import datetime

#1 Substarct five days from the current date
cur_date = datetime.datetime.now()
new_date = cur_date - datetime.timedelta(days=5)

print(cur_date)

#2 Yesterday, Today, Tomorrow
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
yesterday = today - datetime.timedelta(days=1)

#3 Drop microseconds
d = datetime.datetime.now()
print(d.strftime("%Y-%m-%d %H:%M:%S"))

#4 Date difference in seconds
d1 = input("day-month-year: ")
d2 = input("day-month-year: ")

f_d1 = datetime.datetime.strptime(d1, "%d-%m-%Y")
f_d2 = datetime.datetime.strptime(d2, "%d-%m-%Y")

print(abs(f_d1 - f_d2).total_seconds())


