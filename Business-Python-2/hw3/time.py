import datetime

d1 = datetime.datetime(2010, 3, 2, 12, 15, 0)
print(d1)

diff = datetime.timedelta(days=145, hours=10, minutes=3)  
#145天10小時又3分鐘

d2 = d1 + diff
print(d2)