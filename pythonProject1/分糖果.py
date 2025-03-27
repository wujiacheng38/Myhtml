def distribute_candies(n, candies):
    cnt = 0
    while True:
        if all(candy == candies[0] for candy in candies):
            break
        new_candies = [0] * n
        for i in range(n):
            if i == 0:
                new_candies[n - 1] = candies[i] // 2
            else:
                new_candies[i - 1] = candies[i] // 2
        for i in range(n):
            candies[i] = new_candies[i] + candies[i] // 2
            if candies[i] % 2 != 0:
                candies[i] += 1
                cnt += 1
    return cnt

n = int(input())
candies = list(map(int, input().split()))
result = distribute_candies(n, candies)
print(result)