# Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime
now = datetime.now()
print(now)
timestamp = now.timestamp()
print(timestamp)
# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
current_day = now.strftime("%m/%d/%Y, %H:%H:%S")
print(current_day)
# Today is 5 December, 2019. Change this time string to time.
from datetime import date
hoje = date(2019,12,5)
print(hoje)
# Calculate the time difference between now and new year.
now = date(2025,12,15)
newyear = date(2026,1,1)
diff = newyear - now
print(diff)
# Calculate the time difference between 1 January 1970 and now.
Unix_timestamp_day = date(1970,1,1)
diff = now - Unix_timestamp_day
print(diff)
