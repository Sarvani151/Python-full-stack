#math module
'''import math
print(math.pi)
print(math.pi*3)
print(math.sqrt(2))
print(math.pow(2,2))
print(math.log(10))
print(math.tan(45))
print(math.cos(60))
print(math.sin(30))
print(math.ceil(4.9))
print(math.floor(6.9))'''

'''from math import pi,sqrt,log,tan,cos
print(pi)
print(sqrt(2))
print(log(20))
print(tan(45))
print(cos(60))'''

#sys module
'''import sys
print(sys.path)
print(sys.version)'''

#os module
'''import os
print(os.path)
print(os.getcwd())
print(os.listdir())
print(os.mkdir("july27"))'''

#random module
'''import random
a=[10,20,30,60,80]
b=random.choice(a)
print(b)'''

'''import random
a=random.randint(20,50)
print(a)'''

'''mport random
a=[10,30,50,60,80]
b=random.choice(a)
print(b)'''

#DICE CODE
'''import random
while True:
    input("enter the roll of dice")
    a=random.randint(1,6)
    print(a)
    option=input("roll again?(y/n)")
    if option=="y":
        continue
    elif option=="n":
        break
    else:
        print("invalid option")'''

#CALENDAR CODE
'''import calendar
year=2026
month=8
print(calendar.month(year,month))'''

'''import calendar
year=2026
print(calendar.calendar(year))'''

'''import calendar
a=int(input("enter the year"))
b=int(input("enter the month"))
print(calendar.month(a,b))'''

#date
'''from datetime import date
a=date.today()
print(a)'''

'''import datetime
a=datetime.datetime.now()
print(a)'''
#epoch time
'''import time
a=time.time()
print(a)'''
#local time
'''import time
a=time.time()
b=time.localtime(a)
#print(b)

#print(f"today is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")
#print(f"time is {b.tm_hour}:{b.tm_min}:{b.tm_sec}")
print(f"day is {b.tm_wday}-{b.tm_yday}-{b.tm_isdst}")'''

'''import random
a=random.randint(10)
time.sleep(20)
print(a)'''
#error handling
#syntax error
'''for i in range(10):
print(i)'''

#run_time error
'''a=int(input("a value"))
b=int(input("b value"))
print(a//b)'''#10//0->zero divison error

#logical error
'''a=10
b=20
if a<b:
    print("less")'''
a=10
b=20
if a>b:
    print("true")#no output








