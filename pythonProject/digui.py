#递归你是真抽象

#两个递归对象
# def hannuota(N,A,B,C): #分别代表层数、起始点、辅助杆、目标位置
#     if N == 0:
#         return
#     #N-1个盘子从A挪到B
#     hannuota(N-1,A,C,B)
#     #第N个盘子从A挪到C
#     print('{}->{}'.format(A,C))
#     #N-1个盘子从B挪到C
#     hannuota(N-1,B,A,C)
# hannuota(3,'塔1','塔2','塔3')


#阶乘
# def jiecheng(n):
#     #定义递归出口
#     if n <= 1:
#         return 1
#     #递归方程
#     res = n * jiecheng(n-1)
#     return res
# print(jiecheng(int(input())))


#lanqiao760
#多个递归对象
def f(n):
    if n == 1:
        return 1
    ans = 1

    for i in range(1, n // 2 + 1):
        ans += f(i)
    return ans
print(f(6))

