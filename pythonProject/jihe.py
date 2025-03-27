# #注意空字典，不是空集合
# s = {}
# print(type(s))
#
# #集合的几种创建方式  法1
# s = {1,2,3}
# print(type(s))

# #法2  利用set()  对象一般是列表和元组
# s = [1,2,3]
# print(type(s))
# x = set(s)
# print(x)
# print(type(x))

#法3  字典到集合
# a = ['a','b','c']
# b = ['你','是','猪']
# c = dict(zip(a,b))
# print(c,type(c))
# d = set(c)
# e = set(c.values())
# f = set(c.items())
# print(d)
# print(e)
# print(f)

# #集合中若存在重复元素，只显示一个
# s = {1,1,1,1,1}
# print(s)

# #遍历集合 和遍历列表是一样的
# s = {1,2,3}
# for i in s:
#     print(i)
# print(sum(s),max(s),min(s))


#输入若干数字，将所有数字去重后，输出数字个数   / 计算有多少重复的数字
# s = [1,2,3,2,3,4,2,1,3,212,21]
# x = set(s)
# cont = len(x)
# print(cont)
