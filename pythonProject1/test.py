# #排列树
# #定义一颗树，首先得确实它的高度吧
# n = int(input())
# x = int(input())
# path = []
# vis = [False] * (x+1)
# def dfs(depth):
# #比如去摘一个苹果，但你不知道在哪里，要遍历一棵树对吧，一步一步遍历,到最后一层遍历结束
#     if depth == n:
#         #这条路的路径，我看看是咋走的
#         print(path)
#         return
# #遍历这棵树的方式，重复的我不想要去看了，每层有x段树枝，我一段一段去找,找过的我要记录下来
#     for i in range(1,x+1):
#         if vis[i]:
#             continue
#         #记录下找过的路并标记，防止重新走相同的路
#         path.append(i)
#         vis[i] = True
#         #接着找下一层
#         dfs(depth+1)
#         #一条路走完了，清空标记走第二条(每条路上是不一样的虽然某些地方与前一条相同)，循环往复
#         vis[i] = False
#         path.pop()
# dfs(0)
#
#

#小蓝要买m重量的瓜，每个瓜的重量为Ai,(小蓝可以买半个瓜，买半个等价于小蓝劈了一刀)
#分析，，买半个/买一个  ->  重量到m  就不买
n,m = mp(int,input().split())
A = list(map(int,input().split()))
m *= 2
A = [i*2 for i in A]

# # 此时树的深度 = 瓜的数量
# def dfs(depth,weight,cnt):
#     #一些剪枝操作  如果买的瓜的重量超过m，即不满足条件
#     if weight > m:
#         return
#     if weight == m:
#         global ans
#         ans = min(ans,cnt)
#     if depth == n:
#         return
#     #买瓜  买一半，买一个，不买  三种情况
#     dfs(depth+1,weight+0,cnt+0)
#     dfs(depth+1,weight+A[depth],cnt)
#     dfs(depth+1,weight+A[depth]//2,cnt+1)
#
# ans = n+1
# dfs(0,0,0)
# if ans == n+1:
#     print(-1)
# print(ans)