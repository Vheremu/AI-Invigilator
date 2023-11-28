import time,datetime
from sittings.models import Sitting
def timeleft(Sitting):
    sitting=Sitting
    print(sitting)
    date = sitting.schedule
    date = datetime.datetime(date.year,date.month,date.day,date.hour,date.minute,date.second)
    print(date)
    now = datetime.datetime.now()
    print(now)
    left = date-now
    print(left.total_seconds())
    print(left)
    return left
# h = time.time()
# print(h)
# x = input('please stop the clock')
# v = time.time()
# y = str(round(v-h))
# print('there have been :+'+y+' seconds since program started')
# for i in range(1000):
#     date = datetime.datetime(2023,7,10,0,0,0)
#     # x=str(date.hour)
#     # y=str(date.minute)
#     # z=str(date.second)
#     # print(date)
#     # print(x+':'+y+':'+z)
#     # # h=str(datetime.hour)
#     # # m=str(date.minutes)
#     # # n=str(date.seconds)
#     # # print(h+','+m+','+n)
#     # print('tick')
#     # time.sleep(1)
#     # print('tock')
#     # time.sleep(1)
#     date2 = datetime.datetime.now()
#     date3 = date2 - date
#     x = str(date3.days)
#     y = '45'
#     z = str(round(date3.seconds))
#     print(date3)
#     print(x+'days '+y+'hours '+z+'seconds')
#     time.sleep(1)
