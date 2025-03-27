#动态规划之0-1背包
def knapsack(n,w,v,c):
#构建一个n+1行，c+1列矩阵
    d = [[0]*(c+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,c+1):
            if j<w[i]:
                d[i][j] = d[i-1][j]
            else:
                d[i][j] = max(d[i-1][j],d[i-1][j-w[i]]+v[i])
    return d[n][c]

n,c = map(int,input().split())
w = [0] * (n+1)
v = [0] * (n+1)
for i in range(1,n+1):
    w[i],v[i] = map(int,input().split())
print(knapsack(n,w,v,c))











# #动态规划的思想(最优子结构)
# n,c  = map(int,input().split())
# #定义物品重量和价值
# w = [0]*(n+1)
# v = [0]*(n+1)
# for i in range(1,n+1): #n个物品   索引定义为1~n
#     w[i],v[i] = map(int,input().split())
# def knapsack(w,v,n,c):  #分别表示物体的体积、价值、数量,背包的容量
#     #构建一个二维矩阵
#     matrix = [[0]*(c+1) for _ in range(n+1)]
#     for i in range(1,n+1):
#         for j in range(1,c+1):
#             if w[i] > j:   #物体的体积大于背包的容量
#                 matrix[i][j] = matrix[i-1][j]
#             else:
#                 matrix[i][j] = max(matrix[i-1][j],matrix[i-1][j-w[i]]+v[i])
#     return matrix[n][c]
# print(knapsack(w,v,n,c))
