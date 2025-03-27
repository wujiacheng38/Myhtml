#支持日期和时间的运算  包含四种数据  date、time、datetime,timedelta


# import datetime
# #定义date   传递年月日
# t = datetime.date(2025,2,23)
# print(t)
# #
# # #获取年月日
# print(t.year,t.month,t.day)
# #周几  0-6  0表示周一
# print(t.weekday())

# #日期之间允许加减
# a = datetime.date(2025,2,24)
# b = datetime.date(2025,3,8)
# c = b - a
# print(c)
# print(a.weekday(),b.weekday())
# #日期之间支持比较
# if a >= b:
#     print('a >= b')
# else:
#     print('a < b')

#定义time  传递时分秒
# t1 = datetime.time(22,44,55)
# t2 = datetime.time(22,55,55)
# print(t1,'\n',t2)

#时间直接不允许加减，但支持比较
# t3 = t2 > t1
# print(t3)

# #获取年月日
# t1 = datetime.time(22,44,55)
# print('hour:',t1.hour,'   minitue:',t1.minute,'   second:',t1.second)

#定义datetime 传递年月日 时分秒
# t = datetime.datetime(2025,5,20,4,20,25)
# print(t,type(t))
# #定义datetime  也可通过合并日期和时间
# t1 = datetime.date(2025,2,23)
# t2 = datetime.time(22,55,55)
# t3 = datetime.datetime.combine(t1,t2)
# print(t3)
# #datetime支持比较和加减
# t4 = t - t3
# print(t4.days)
# print(t > t3)
# print('--------------')
#
# #timedelta（时间间隔）   用days、sceonds、microseconds这三个变量来存储时间间隔
# delta =  datetime.timedelta(days = 100,seconds= 1)
# print(delta,type(delta))
# print(delta.seconds)  #转化成秒
# print(delta.total_seconds())   #统一转化成秒
# #日期时间可以与时间间隔进行加减操作
# print(t + delta)

# #日期、时间、日期时间  都可以转化成字符串
# t = datetime.datetime(2025,5,20,4,20,25)
# str_time = t.strftime('%Y-%m-%d %H:%M:%S')
# print(str_time,type(str_time))
# #字符串 转化成日期、时间、日期时间
# time = datetime.datetime.strptime(str_time,'%Y-%m-%d %H:%M:%S')
# print(time,type(time))
#
# #获取当前日期、日期时间
# currernt_date = datetime.date.today()
# currernt_datime = datetime.datetime.now()
# print(currernt_date,'      ',currernt_datime)