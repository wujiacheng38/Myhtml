#从小到大

#lanqiao3225
#选择排序
# n = int(input())
# #a = [int(i) for i in input().split()]
# a = list(map(int,input().split()))
# #从小到大排序
# for i in range(n-1):
#     idx = i
#     for j in range(i+1,n):
#         if a[idx] > a[j]:
#             idx = j
#     a[i],a[idx] = a[idx],a[i]   #这里要交换而不是赋值，赋值会导致数据丢失
# for i in range(n):
#     print(a[i],end=' ')
#print(*a)

#插入排序
#默认第一个数有序，对n-1个数进行排序
# n = int(input())
# a = list(map(int,input().split()))
# for i in range(1,n):
#     #插入的那个数最小就放在最前天，不是最小，则插入到比它小的数的后边
#     insert_idx = 0
#     value = a[i]
#     for j in range(i-1,-1,-1):
#         if value < a[j]:
#             #往后挪
#             a[j+1] = a[j]
#         else:
#             insert_idx = j+1
#             break    #找到插入位置即刻退出
#     a[insert_idx] = value
# print(*a)
# print(' '.join(map(str,a)))
# for i in a:
#     print(i,end=' ')


# 冒泡排序
# n = int(input())
#arr = [int(i) for i in input().split()]
# arr = list(map(int,input().split()))
# for i in range(n-1):
#     for j in range(n-1-i):
#         if(arr[j] > arr[j+1]):
#             arr[j],arr[j+1] = arr[j+1],arr[j]
# #输出的三种写法
# print(*arr)
# print(' '.join(map(str,arr)))
# for i in arr:
#     print(i,end=' ')



#----经典的递归与分治策略
'''
快速排序
二分查找
归并排序
'''

#快速排序
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     #分解
#     #找基准值和基于基准值分为小于基准和大于基准的左右两部分
#     pivot = arr[0]
#     left = [x for x in arr[1:] if x<=pivot]
#     right = [x for x in arr[1:] if x>pivot]
#     #递归解决该子问题并合并
#     return quick_sort(left) + [pivot] + quick_sort(right)
# arr = [38,27,43,3,9,82,10]
# sorted_arr = quick_sort(arr)
# print(sorted_arr)





#归并排序
# def merge_sort(arr):
#     #递归条件
#     if len(arr) <= 1:
#         return arr
#     #分解
#     #递归方程
#     mid = (len(arr))//2
#     L = merge_sort(arr[:mid])
#     R = merge_sort(arr[mid:])
#     #合并
#     return merge(L,R)
#
# def merge(L,R):
#     result = []
#     l = r = 0
# #这里还有种方法while len(L) ！= 0 and len(R) ！= 0
#     while len(L) > l and len(R) > r:
#         if L[l] < R[r]:
#             result.append(L[l])
#             l += 1
#         else:
#             result.append(R[r])
#             r += 1
#     result.extend(L[l:])
#     result.extend(R[r:])
#     return result
#
# arr = [38,27,43,3,9,82,10]
#
# print(merge_sort(arr))


# import time  #常用于计时
# a = time.time()
# def binary_search(arr,target):
#     left,right = 0 ,len(arr)-1
#     while left <= right:
#         mid = (left + right) // 2
#         if (arr[mid] == target):
#             return  mid
#         elif(arr[mid] < target):
#             left = mid + 1
#         else:
#             right = mid -1
#     return -1
# time.sleep(1)
# b = time.time()
# print('{:.4f}'.format(b-a))
# arr = [1,3,9,10,27,38,43,82]
# target = 38
# index = binary_search(arr,target)
# print(index)


#合并两个有序数组使之成为一个有序数组
# def merge(A,B):
#     result = []
#     i = j = 0
#     while len(A) > i and len(B) > j:
#         if A[i] < B[j]:
#             result.append(A[i])
#             i += 1
#         else:
#             result.append(B[j])
#             j += 1
#     result.extend(A[i:])
#     result.extend(B[j:])
#     return result
# A= [2,3,4]
# B= [1,6,7]
# sorted_arr =merge(A,B)
# print(sorted_arr)



