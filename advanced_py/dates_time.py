from datetime import datetime, timezone, timedelta

print(datetime.now())  # <- is a "naive" datatime object, which means there is no
# timezone reference.

print(datetime.now(timezone.utc))

today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)


print(today)
print(tomorrow)

print(today.strftime('%d-%m-%Y %H:%M:%S'))  # <- strftime: string format time

userdate = input('Enter the date in YYYY-mm-dd: ')
userdate = datetime.strptime(userdate, '%Y-%m-%d')  # <- strptime: string parse time.

print(userdate)

