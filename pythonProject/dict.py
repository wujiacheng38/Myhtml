#创建一个空字典
# a = {}

#创建字典的策略，需要满足
#1.key  不能重复，value无限制
#2.key 必须是字符串，数字，元组不可变的类型

#字典中的key和value直接用冒号分割，元素之间用逗号分隔
#字典的key只能为数字、字符串、元组，大多情况适用字符串作为key
#value 类型没有限制
#创建字典 1.直接创建

# a = {(1,2):123,1:456,0:789}
# print("type(a = ",type(a))
# print(a)
# #创建字典 2.利用dict+赋值，此时key只能是字符串，不能是数字
# b = dict(a = '你好帅',b= '阿莹',c = 25)
# print(b)

# # #创建字典 3.利用dict+列表/元组
# c1 = dict([['a',123],['b',234],['c',567]])
# c2 = dict([('a',123),('b',234),('c',567)])
# print(c1,type(c1))
# print(c2,type(c2))
#
# #创建字典 4. 利用zip
# #把多个序列相同的下标元素组装成元组，结果是一个可迭代对象
# x = ['1','2','3']
# y = ['你','真','棒']
# z1 = dict(zip(x,y)) #z1直接在迭代器上操作，不需要额外内存来存储中间列表
# z2 = list(zip(x,y))  #可以利用list将key列表和value列表进行组装
# z3= dict(list(zip(x,y)))   #现将迭代器转换为列表,在创建字典，会占用额外内存
# print(z1,type(z1))
# print(z2,type(z2))
# print(z3,type(z3))

# #访问字典  把key下标，get()方法
# #pyrhon的字典通过key来获取value，把key看做下标即可
# a ={'1': '你', '2': '真', '3': '棒'}
# print(a['1'])
# #如果事先并不知道x是否在字典中的key中，需要查询字典中x对应的value，可以使用get方法
# #a.get(x,value=None)  a表示字典，x表示查询的key,value表示默认值
# print(a.get('1'))
# print(a.get('4','no exit'))

# #添加元素
# a ={}
# a['语文'] = 80
# print(a['语文'])
# print(a)
# #修改元素
# a['语文'] = 80
# a['语文'] = 84
# print(a)
# #删除字典中的键值对 1.可用python本身的删除语法 del
# a['语文'] = 80
# del a['语文']
# print(a)
# #删除字典中的键值对 2.也可用字典的删除方法pop
# a ={'1': '你', '2': '真', '3': '棒'}
# a.pop('1')
# print(a)
#
# #遍历字典
# #1.与list 一样，直接利用for语句就可以遍历字典
# a ={'1': '你', '2': '真', '3': '棒'}
# for x in a:
#     print(x,end=':')
#     print(a[x],end='')

#2.利用a.keys(),a.values,a.items()可以分别循环遍历key、value、二元组（key,value）
# a ={'1': '你', '2': '真', '3': '棒'}
# for x in a.keys():
#     print(x)
# for x in a.values():
#     print(x)
# for x,y in a.items():
#     print(x,y)

# #判断是否存在元素  是用in/not in
# w = {'1':'hello','2':'world','3':'!'}
# print( '1' in w)
# print('1' in w.keys())
# print('hello' in w.values())
# print(('1','hello') in w.items())

# #拷贝字典  需要用到copy（）
# #与list类似   直接赋值相当于去别名
# w = {'1':'hello','2':'world','3':'!'}
# s = w
# print(s)

#列表可直接相加合并而字典不行
#合并两个字典 利用update()可以将一个字典的key-value对更新到已有字典中
a = {1:1,2:2}
b = {3:3,4:4}
a.update(b)
print(a)