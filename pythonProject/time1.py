import time1  #常用于计时

# #计算程序运行了多久

a = time.time()
ans = 1
time.sleep(1)
for i in range(10):
    ans = ans * (i+1)
print(ans)
b = time.time()
print('{:.4f}'.format(b-a))
print(type(a))

# #获取本地时间
# t = time.localtime()
#
# print(t,"\n",type(t),"\n",t.tm_wday,'\n',t.tm_yday)
#
# # #把时间按照format格式转换,返回一个字符串
# t = time.localtime()
# print(type(t))
# str_t = time.strftime("%Y-%m-%d %H:%M:%S",t)
# print(type(str_t),str_t)
# # #把字符串按照format格式转换,返回一个时间
# t1 = time.strptime(str_t,"%Y-%m-%d %H:%M:%S")
# print(type(t1),t1)



