#替换字符串中的元素

# a= '11111111111cat'
# s = a.replace('cat','222',)
# print(a)
# print(s)

#去掉字符串中的空格或指定的字符 strip()、lstrip()、rstrip()
# a = ' lov e me? '
# s = a.strip(' o l v e?')
# print(a)
# print(s)

# #计算字符串中出现指定字符的次数
# a = '1021,0211'
# s = a.count(input(),6)
# print(s)

# #查找字符串中的元素是否存在
# a ='10210211'
# while True:
#     s = a.find(input())
#     if s == -1:
#         print('未找到该字符')
#         break
#     else:
#         print('字符在{}位置'.format(s))

#字符串转换成列表的方法
# a = ' hello world'
# s = a.split()  #法1 ；利用字转串分隔符->列表
# b = list(a)    #法2 ：直接使用list函数
# print(b)
# print(s)

#列表转成字符串
# list1 =['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!']
# string = ''.join(list1)
# print(string)

#一行输入两个整数，输入两数之和
# a,b = map(int,input().split())
# print(a+b)

#一行输入若干个数字，求这些数字之和
# intlist = [int(i) for i in input().split()]
# intlist1 = list(map(int,input().split()))
# print(intlist)
# print(intlist1)
# print(sum(intlist),sum(intlist1))

#修改字符串  法1  变成列表，修改完成后，在利用join()变回字符串
a = '你好'
b = list(a)
b[0] = '我'
print(b)
c = ''.join(b)
print(c)
#修改字符串  法2 利用切片+重新拼接字符串
# a = 'hello.world!'
# b = a[:6]+'python!'
# print(b)
##修改字符串  法2 利用replace()
# a = 'shiyingbaby'
# b = a.replace('baby','baobao')
# print(b)

#字符串的输出 用format   保留小数的时候策略采用的是四舍五入
#将值插入到字符串中的位置，进行格式化
# pai = 3.1415926
# a = 10000
# s = 12
# print('{:.2%}'.format(pai))  #百分数
# print('{:e}'.format(a))    #科学计数法
# print('{:d}'.format(a))   #10进制
# print('{:b}'.format(a))     #2进制
# print('{:x>4}'.format(s))   #向右填充  宽度为4

#两种字符串翻转方法
#利用切片和函数
# x1 = " dou you know"
# x2 = ''.join(reversed(x1))
# x3 = x1[::-1]
# print((x2))
# print((x3))