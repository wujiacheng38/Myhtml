#定义一个类  class + 类名
#__init__(self)是一种构造函数，可以包含多个参数，但必须包含self参数
#且self必须为第一个参数，self不需要手动传递单数

#
# class student:
#     #类的属性
#     x = 'hello'
#     #初始化方法，初始化一个对象
#     def __init__(self,name,sex):
#         #对象的属性
#         self.name = name
#         self.sex = sex
# #类的实例化  格式：类名(参数） 这里放的参数会传入__init__构造函数中
# a = student('吴佳成','男')
# b = student('时莹','女')
# print(a.name,a.sex)
# print(b.name,b.sex)
# print(student.x)

# #实例方法的调用  内部/外部
# class Dog:
#     def __init__(self,name):
#         self.name = name
# #定义实例方法(自动绑定到实例)
#     def bark(self):
#         print('{}汪汪!'.format(self.name))
#         self.eat() #在方法内通过self调用其他实例方法
#     def eat(self):
#         print('{}吃东西'.format(self.name))
# #创建实例对象
# a = Dog("旺财")
# #调用实例方法的方式1：通过实例名.方法名
# print(a.bark())   #外部调用实例方法

# class student:
#     school = 'NBA SCHOOL'
#     def __init__(self,name,sex):
#         self.name = name
#         self.sex = sex
#     #类方法
#     @classmethod  # 适用于需要访问或修改类级别数据的方法。它接收类本身作为第一个参数 (cls)
#     def get_sex_list(cls):  #此处cls和self类似，cls对应整个class，self对应的是某个对象
#         return cls.school
#     @staticmethod   #不需要self或cls  适用于与类相关但不依赖于类或实例状态的方法。它不能访问或修改类或实例的属性。
#     def test():
#         print('Hello World')
#         return 'Test completed'
# a = student.get_sex_list()
# b = student.test()
# print(b)