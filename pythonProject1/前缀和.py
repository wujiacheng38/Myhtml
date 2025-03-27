#  前缀和的定义  prefix_sum[i] = nums[0] + nums[1] + ... + nums[i-1]
#求数组的前几项和
nums = list(map(int,(input().split())))


#构建一个前缀和数组
def build_prefix_sum(nums):
    n = len(nums)
    prefix_sum = [0] * (n+1)
    for i in range(1,n+1):
        prefix_sum[i] = prefix_sum[i-1]+ nums[i-1]
    return prefix_sum

#区间和计算
def range_sum(prefix_sum,left = 1,right = 3):
    return prefix_sum[right+1] - prefix_sum[left]

















# #区间和计算
# def range_sum(nums,left,right):
#     n = len(nums)
#     #构建前缀和数组
#     prefix_sum = [0] * (n+1)
#     for i in range(1,n+1):
#         prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
#     #计算区间和
#     return prefix_sum[right+1] - prefix_sum[left]
#
# print(range_sum(nums,1,3))











