'''import datetime
now = datetime.datetime.now()
print(now.strftime("%d:%m:%Y"))
print(datetime.date.today().month)

x = datetime.datetime(year=2021, month=7, day=9)
y = datetime.datetime(year=2021, month=7, day=8)

diff = x - y
print(diff)

end = datetime.datetime.now()
differ=end-now
print(differ)'''

import datetime
import pytz

today = datetime.date.today()
print(today)
birthday = datetime.date(1994, 3, 30)
print(birthday)

days_since_birth = (today - birthday).days
print(days_since_birth)

tdelta = datetime.timedelta(days=10)
print(today + tdelta)

print(today.month)
print(today.weekday())

a = datetime.time(7, 2, 20, 15)
print(a)

datetime_today = datetime.datetime.now(tz = pytz.utc)
datetime_pacific = datetime_today.astimezone(pytz.timezone('US/Pacific'))
print(datetime_pacific)
for tz in pytz.all_timezones:
    print(tz)









