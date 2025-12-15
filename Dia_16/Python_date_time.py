# python got datetime module do handle date and time
import datetime
print(dir(datetime))
# with dir or help built-in commands it is possible to know the avaible functions in a certain module.
# As you can see, in the datetime module there are many function, but we will focus on date, datetime, time an timedelta

# Getting dateime information
from datetime import datetime
now = datetime.now()
print(now)
day = now.day
month  = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp',timestamp)
print(f'{day}/{month}/{year},{hour}:{minute}')
# timestamp or unix timestamp is the number of seconds elapsed from 1st of january 1970 UTC.

# Formating Date Output Using strtime
from datetime import datetime
new_year = datetime(2020,1,1)
print(print(new_year))
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.hour
second = new_year.second
print(day,month,year,hour,minute)
print(f'{day}/{month}/{year}, {hour}:{minute}')

# Formating date time using strftime method
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print('time one:', time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
print("time two", time_two)

# all_formats = now.strftime("%a, %A, %w, %d, %b, %B, %m, %y, %Y, %H, %I, %p, %M, %,S %f, %z, %Z, %j, %U, %W, %c, %x, %X")

# String tom time Using strptime
from datetime import datetime
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string,"%d %B, %Y" )
print("date_object =", date_object)

# Using date from datetime
from datetime import date
d = date(2020,1,1)
print(d)
print('Current dat: ',d.today())
# date object od todays dat
today = date.today()
print("Current year: ", today.year)
print("Current month: ",today.month)
print("Current day: ", today.day)

# Time object to represent time
from datetime import time
a = time()#hout = 0, minute = 0, second = 0
print("a = ", a)
# time(hour, minute and second)
b = time(10,30,50)
print("b = ",b)
# time hour, minute and second
c = time(hour=10,minute=30,second=50)
print("c = ",c)
# time hoot, minute, second, microsecond
d = time(10,30,50,200555)
print("d = ",d)

# Difference Between two point in time Using
today = date(year=2019, month=12, day=5)
new_year = date(year=2020,month=1,day=1)
time_left_for_newyear = new_year - today
print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(year = 2019, month=12, day=5, hour=0,minute=59,second=0)
t2 = datetime(year=2020, month=1,day=1, hour=0,minute=0,second=0)
diff = t2 - t1
print('time left for newyear: ', diff)

# Difference Between two point in time using timedelta
from datetime import timedelta
t1 = timedelta(weeks=12, days=10,hours=4, seconds=20)
t2 = timedelta(days=7,hours=5,minutes=3,seconds=30)
t3 = t1 - t2
print("t3 =", t3)

