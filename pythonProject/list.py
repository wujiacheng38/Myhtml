# #列表的添加可以用extend()、append()、insert()
# a = []
# a.append(123)  #单个元素
# print(a)
# a.extend([123,456]) #可以是列表、元组等可迭代对象
# print(a)
# a.append([123,456])  #把[123,456]看成了单个元素  即括号内的
# print(a)
# a.insert(3,567)
# print(a)
# print('---------')

a = [1,2,3,4,5]
# #要实现在列表的任意位置插入若干元素方法1：切片
# a[1:1] = [222,333,444]
# print(a)
#方法2:先切片再拼接
# print(a[:4]+[555,666]+a[4:])
# #方法3：利用循环+insert()
# nums = [777,888]
# pos = 2
# for num in nums:
#   a.insert(pos,num)
#   pos += 1
# print(a)


# #列表中删除元素可以用del、pop、remove
# #del 和 pop()的主要区别在于是否具有返回值
# del a[1]
# print(a)
# s=a.pop(2)
# print(a)
# print(s)
# print('---------')
# d = a.remove(123)  #remove()  是按值删除
# print(a)
# print(d)


# #如果一个列表中有多个  我想要删除的元素(假定为x)
# print('---------')
# list = [1,2,3,4,2,3,4,2,2,2,2,1]
# x = int(input())
# while x in list:
#   list.remove(x)
# print(list)

# #查找列表中某个元素出现的次数
# a = [1,2,2,2,2,2,3,3,1,1,1]
# s = a.count(2)
# print(s)
# #在列表中查找元素出现的位置
# pos = a.index(1,4)
# print(pos)
# a.clear()
# print(a)

# #拷贝列表
# #与字典类似  直接赋值相当于去别名
# a = [1,2,3]
# s = a
# s[0] = 3  #修改s，a也一起修改
# print('a=',a,'s=',s)
# #需要借助copy()函数，
# b = [1,2,3]
# d = b.copy()
# b[0] = 3   #修改b,d不变
# print('b=',b,'b=',d)

# #合并列表
# a = [1,2,3]
# b = [2,3,4]
# c = a+b
# print(c)


