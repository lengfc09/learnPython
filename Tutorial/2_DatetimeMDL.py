import datetime
d = datetime.date(2016, 7, 24)
tday = datetime.date.today()
print("Today is:", tday)
# print(tday.day)
# print(tday.year)
# print(tday.month)
# print(tday.weekday())
# print(d.isoweekday())


tdelta = datetime.timedelta(days=7)
print(tdelta + tday)
tdelta2 = tday - d
print(tdelta2)
print(tdelta2.total_seconds(), "seconds")

# t = datetime.time(9, 30, 45, 100000)
# print(t)


t = datetime.datetime.today()
print(t)

print(t.isoformat())
print()
