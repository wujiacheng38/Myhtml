# #基础做法  当N,Q数值非常大的时候时间复杂度会非常的高
# N,Q = map(int,input().split())
# LIST = [int(i)for i in input().split()]
# for i in range(Q):
#   l,r,x = map(int,input().split())
#   for i in range(l-1,r):
#     LIST[i] = LIST[i] + x
# LIST1 = [i if i>=0 else 0 for i in LIST  ]
# #LIST1 = list(map(lambda i: i if i >= 0 else 0, LIST))
# print(*LIST1)
# #print(' '.join(map(str,LIST1)))


#差分   定义:diff[1] = a[1]   diff[i] = a[i] - a[i-1]
#差分数组的前缀和等于原数组  diff[1] + diff[2] = a[1] + a[2] - a[1] = a[2]


N,Q = map(int,input().split())
LIST = [int(i)for i in input().split()]
#构建一个差分数组
diff = [0] * (N+1)
diff[0] = LIST[0]
for i in range(1,N):
  diff[i] = LIST[i] -LIST[i-1]

for i in range(Q):
  l,r,x = map(int,input().split())
  l = l -1
  r = r -1
  diff[l] = diff[l] + x
  diff[r+1] = diff[r+1] - x
  print(diff)
# #还原数组（前缀和）
LIST[0] = diff[0]
for i in range(1,N):
  LIST[i] = LIST[i-1] + diff[i]

LIST1 = [i if i >= 0 else 0 for i in LIST]
print(*LIST1)


