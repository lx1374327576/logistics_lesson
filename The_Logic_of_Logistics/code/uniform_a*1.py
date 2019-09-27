import random
import copy

# 箱子大小100 重复10000次求平均
avg1 = 0
avg2 = 0
v = 1000000
T = 3
L = 100
for k in range(1, T + 1, 1):
    ans = 0
    for p in range(10):
        a = []
        for i in range(L ** k):
            a.append(random.randint(1, v))
        a.sort()
        b = copy.deepcopy(a)

        # 启发式1 一个箱子两个物品
        ans1 = 0
        i = 0
        j = (L ** k) - 1
        while i < j:
            if a[i] + a[j] <= v:
                i += 1
                j -= 1
                ans1 += 1
            else:
                j -= 1
                ans1 += 1
        if i == j:
            ans1 += 1
        ans += ans1
    ans = ans / (L ** k) / 10
    print(ans)
