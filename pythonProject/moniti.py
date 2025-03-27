#模拟题：直接按照题目含义模拟即可，一般不涉及算法
#注意：1.读懂题：理清楚题目流程
#     2.代码和步骤一一对应，变量名、函数名、函数功能
#     3.提取重复的部分，写成对应的函数(子模块)
#     4.按顺序写、分块调试

# #lanqiao143
# n = int(input())  #初始买入的饮料瓶数
# ans = n   #喝到的饮料数
# while n >= 3:
#     ans = ans + n // 3
#     n = n % 3 + n//3
# print(ans)

#lanqiao550
# n,m = map(int,input().split())
# #读取二维数组
# Map = []
# for i in range(n):
#     a = list(map(int,input().split()))
#     Map.append(a)
# #构建结果矩阵:创建一个与输入矩阵大小相同的全零矩阵 ans，用于存储模糊后的结果。
# ans =[[0]*m for i in range(n)]
#
# #遍历二维数组
# for i in range(n):
#     for j in range(m):
#         #遍历每个位置，求出模糊后的结果
#         #（i-1,j-1),（i-1,j),（i-1,j+1)
#         #（i,j-1),  （i,j),  （i,j+1)
#         #（i+1,j-1),（i+1,j-1),（i+1,j-1)
#         #遍历周围的3*3区域
#         tot,cnt = 0,0 #分别表示总和 和 个数
#         # 用于表示当前位置周围 3x3 区域的偏移量
#         for delta_x in [-1,0,1]:
#             for delta_y in [-1,0,1]:
#                 x = i + delta_x
#                 y = j + delta_y
#                 #判断坐标(x,y)是否合法
#                 if 0 <= x< n and 0 <= y <m:
#                     tot += Map[x][y]
#                     cnt += 1
#         ans[i][j] = tot // cnt
#
#
# for a in ans:
#     print(*a)  #利用解包，默认按照空格分隔
    # print(" ".join(map(str, a)))
#M = ('1','2','3')
#* 是解包操作符（Unpacking Operator），用于将列表、元组等可迭代对象解包为独立的元素
#print(*M,sep='.')  #sep 默认是空格


'''
解包操作符 * 只能用于可迭代对象：例如列表、元组、集合、字符串等。
解包后的元素数量必须匹配：a, b, c = [1, 2] 
** 是字典解包操作符，用于解包字典的键值对
'''

#lanqiao156
#斜着走 等等  完成这题想想
n,m = map(int,input().split())
r,c = map(int,input().split())
Map = [[0]*m for i in range(n)]
x,y = 0,0
value = 1
Map[x][y] = value
while value < n * m:
    #向右走
    while y+1 < m and Map[x][y+1] == 0:
        y = y+1
        value = value + 1
        Map[x][y] = value
    #向下走
    while x+1 <n and Map[x+1][y] == 0:
        x = x+1
        value = value + 1
        Map[x][y] = value
    #向左走
    while y-1 >= 0 and Map[x][y-1] == 0:
        y = y-1
        value = value + 1
        Map[x][y] = value
    #向上走
    while x-1 >= 0 and Map[x-1][y] == 0:
        x = x-1
        value = value + 1
        Map[x][y] = value
# for i in Map:
#     print(' '.join(map(str,i)))
print(Map[r-1][c-1])

