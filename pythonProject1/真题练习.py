#
# def f(x):
#     n = 1
#     while x>0:
#         x = x - n
#         n = n + 1
#         if x == 0:
#             break
#         if x<0:
#             return 1
#
#
# n = int(input())
# li = list(map(int,input().split()))
# cnt = 0
# for i in li:
#     if f(i):
#         cnt +=1
# print(cnt)

# a, b = 0, 1
# for i in range(1, 1200):
#     a += i
#     b *= i
#     if (a - b) % 100 == 0:
#         print(i)

# 1 3 24 175 199 200 224 375 399 400 424 575 599 600 624 775 799 800 824 975 999 1000 1024 1175 1199
print(2024041331404202 // 200 * 4 + 2)