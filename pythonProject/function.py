# #定义一个阶乘函数
# def jiecheng(n):
#     res = 1
#     for i in range(1,n+1):
#         res = res * i
#     return res
# print(jiecheng(10))

# #函数中可以有多个return 但只会运行其中一个，碰到return语句，运行结束
# def max(a , b):
#     if a > b:
#         return a
#     else:
#         return b
# print(max(4,3))
#
# #return 可以返回多个变量
# def my(str1,str2):
#     return [str1,str2]
# s = my('你好','小帅')
# print(s[0]+s[1])


# #形参和实参

#如何传参不出错？
#在大多数情况下，尽量不要传递列表，字典这种可变数据，即使传参，也尽量不要改动这些参数
#tips（小技巧)：传递可变数据时，可以传递一个副本，这样修改实参也不会发生变化

# def f(x):
#     x *= 2
#     print('这是形式参数 x = {}'.format(x))
# x = 100
# f(x)
# print("这是实际参数 x = {}".format(x))

#传参机制——值传递 不会导致实际参数的变化，这是由于值传递的是数值  是单向的
# #参数为不可变类型 字符串，数字、元组
# def swap(x,y):
#     x,y = y,x
#     print("这是swap函数")
#     print('x = ',x,'y = ',y)
#     print('id(x) = ',id(x),'id(y)',id(y))
#
# x,y ='3','5'
# print('这是主函数')
# print('x = ',x,'y=',y)
# print('id(x) = ',id(x),'id(y)',id(y))
#
# swap('3','5')
#
# print('这是主函数')
# print('x = ',x,'y=',y)
# print('id(x) = ',id(x),'id(y)',id(y))

# #传参机制——引用传递
# #函数中形式参数变化，会导致实际参数一起变化，这是由于传递的是变量
# #参数为可变类型  列表、字典
#
# def f(x):
#     x.append(4)
#     print("这是自定义函数")
#     print("id(x) ",id(x))
# x = [1,2,3]
# s = x.copy()        #创建副本  小tips
# print("这是主函数")
# print("id(x) ",id(x))
# f(s)
# print("x = ",x)

#传参机制——位置参数
#参数个数相同，顺序意义对应
# def f(a,b,c,d,e):
#     print('a=',a)
#     print('a=', b)
#     print('a=', c)
#     print('a=', d)
#     print('a=', e)
# f(1,2,3,4,5) #实参和形参个数相同，顺序一一对应

#传参机制——默认参数
#默认参数：定义函数时，给一个形参默认值，所有默认参数必须放在最后
# def f(a,b,c=3,d=4,e=5):
#     print('a = ', a)
#     print('b = ', b)
#     print('c = ', c)
#     print('d = ', d)
#     print('e = ', e)
# #后三个参数使用默认值
# f(1,2)
# print('---------')
# #c=5,不使用默认值
# f(1,2,5)

# #传参机制——不定义长参数(*)
# #形式参数前加*，表示不定义长参数，可以按照 位置参数 的格式传递多个参数
# #加了星号（*）的参数会以元组（tuple）的形式导入，存放所有会命名的变量参数
# def f(a,b,*argtuple):
#     print('a = ', a)
#     print('b = ', b)
#     print('argtuple = ',argtuple,type(argtuple))  #元组
# f(1,2,3,4,5,6,7,8,)

#传参机制——不定义长参数(**)  可以按照 关键字 参数的格式传递多个参数
# def f(a,b,**argtuple):
#     print('a = ', a)
#     print('b = ', b)
#     print('argtuple = ',argtuple,type(argtuple))  #字典
# f(1,2,c=3,d=4,e=5)

#变量作用域
#局部变量：函数内部的变量，仅作用于函数内部
#全局变量：函数外部的变量，作用于全局
# total = 0
# def f(a,b):
#     total = a + b
#     print("此处是局部变量,total =", total)
# f(3,4)
# print("此处是外部的变量,total =", total)

# a =10
# def f1(a):
#     #这里的a既是形参又是局部变量
#     a = a + 1
#     print('局部：a =', a)
# f1(a)
# print('全局:a =', a)

#如何在函数内部使用全局变量呢？
#使用global声明
# total = 0
# def f(a,b):
#     global total
#     total= a + b
#     print("此处是全局变量,total =", total)
# f(3,4)
# print("此处是全局的变量,total =", total)

# def f1():
#     global num  #num在此处是全局变量
#     num += 10
#     print("this is f1,num = ",num)  #133
# def f2(num):
#     num += 10  #num在此处是局部变量(有局部先局部)
#     print("this is f2,num = ", num)  #143
# def f3():
#     num = 456   #num在这里是局部变量
# num = 123
# print("this is main,num = ",num) #123
# f1()
# f2(num)
# print("this is main,num = ",num)   #133
# f3()
# print("this is main,num = ",num)  #133
# f1()   #143
# f2(num)  #153
# print("this is main,num = ",num)  #143