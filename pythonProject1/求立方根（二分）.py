def cube_root(N, precision=0.001):
    left, right = 0, N
    while right - left > precision:
        mid = (left + right) / 2
        if mid ** 3 < N:
            left = mid
        else:
            right = mid
    return left

# 测试
T = int(input())
for _ in range(T):
    N = int(input())
    result = cube_root(N)
    print("{:.3f}".format(result))