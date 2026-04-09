### Dates ###
from datetime import datetime

now = datetime.now()

print(now.year)
print(now.month)
print(now.day)  
print(now.hour)
print(now.minute)
print(now.second)  

timestamp = now.timestamp()
print(timestamp)

year_2026 = datetime(2026, 1, 1)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)  
    print(date.hour)
    print(date.minute)
    print(date.second)  
    print(date.timestamp())  

print_date(year_2026)


print("------------------")
from datetime import time 

my_time = time(14, 30, 45)
print(my_time.hour)
print(my_time.minute)
print(my_time.second)


print("------------------")
from datetime import date 

my_date = date(2026, 4, 7)
print(my_date.year)
print(my_date.month)
print(my_date.day)

print("------------------")
from datetime import timedelta
delta = timedelta(days=17, hours=8, minutes=48)
other_delta = timedelta(days=10, hours=5, minutes=30)
print(delta - other_delta)

print("------------------")
print(now.strftime("%Y-%m-%d %H:%M:%S"))
