import datetime as dt

print(dt.datetime.now())

aa=dt.datetime.now()-dt.datetime(2020,7,14,16,30,20)
print(aa)

print(aa.total_seconds())

print(dt.datetime.utcnow())