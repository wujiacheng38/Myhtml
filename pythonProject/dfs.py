# # #将一个数字，拆成三个正整数，并要求后一个大于等于前一个
# x = int(input())
# for i in range(1,x):
#     for j in range(1,x):
#         for k in range(1,x):
#             if i+j+k == x and k>=j>=i:
#                 print(i,j,k)

#如果拆成4,5个，n个数字呢？
#用dfs

# n = int(input())
# p = [[0]*n for i in range(n)]
ans = 0
def dfs(depth, n, m):
    #代表搜索深度
    if depth == 7:
        if n == 0 and m == 0:
            global ans
            ans += 1
        return
    #搜索方式
    for i in range(0, 6):
        for j in range(0, 6):
            if 2 <= i + j <= 5 and i <= n and j <= m:
                dfs(depth+1,n-i,m-j)
dfs(0,16,9)
print(ans)


# x,n = map(int,input().split())
# p = [0] * n
# def dfs(depth):
#     #递归出口
#     if depth == n:
#         for i in range(1,n):
#             if p[i] >= p[i-1]:
#                 continue
#             else:
#                 return
#         if sum(p) != x:
#             return
#         print(p)
#         return
#     #递归
#     for i in range(1,x+1):
#       p[depth] = i
#       dfs(depth+1)
# dfs(0)
