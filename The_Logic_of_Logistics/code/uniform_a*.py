import random
import copy

# 箱子大小100 重复10000次求平均
avg1 = 0
avg2 = 0
avg_three = 0
v = 10000
T = 10000
L = 10000
for k in range(T):
    a = []
    for i in range(L):
        a.append(random.randint(1, v))
    a.sort()
    b = copy.deepcopy(a)

    # 启发式1 一个箱子两个物品
    ans1 = 0
    i = 0
    j = L - 1
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
    avg1 += ans1 / T

    # 启发式2 一个箱子不限物品
    ans2 = 0
    i = 0
    j = L - 1
    three = 0
    while i < j:
        flag = 1
        tmp_v = a[i] + a[j]
        if tmp_v > v:
            j -= 1
            ans2 += 1
            continue
        while a[i+1] + tmp_v < v:
            flag = 0
            tmp_v += a[i+1]
            i += 1
        ans2 += 1
        i += 1
        j -= 1
        if flag == 0:
            three += 1
    if i == j:
        ans2 += 1
    avg2 += ans2 / T
    avg_three += three / T
    if k % 100 == 0:
        print(k)
    # print(ans1, ans2)
print(avg1, avg2)
print(avg_three)
