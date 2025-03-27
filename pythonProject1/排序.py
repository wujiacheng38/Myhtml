N = int(input())
array = list(map(int,input().split()))
print(*sorted(array))
print(*sorted(array,reverse= True))
