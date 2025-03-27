#查找元素所在集合的根节点
def findroot(x):
    # while x!=p[x]:
    #     x = p[x]
    # return x
    if x == p[x]:
        return x
    #路径压缩
    p[x] = findroot(p[x])
    return p[x]
#合并x和y这两个集合
def merge(x,y):
    rootx,rooty = findroot(x),findroot(y)
    p[rooty] = rootx  #拿其中一个的根节点作为另一个集合根节点的父节点
#查询集合x和y是否属于同一集合
def query(x,y):
    rootx,rooty = findroot(x),findroot(y)
    return rootx ==rooty

n,m = map(int,input().split())
p = list(range(n+1))
for _ in range(m):
    op,x,y = map(int,input().split())
    if op == 1:
        merge(x,y)
    else:
        print('YES' if query(x,y) else 'NO')