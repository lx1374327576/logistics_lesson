import math
p = 10000


def f(x):
    return math.exp(-(x ** 2) / 2)


def qjf(x_min=1.0, x_max=10000):
    ans = 0
    for x in range(p):
        now_x = x_min + x / p * (x_max - x_min)
        ans += 1/p * f(now_x)
    return ans


for i in range(p):
    if qjf(x_min=i*100/p) / ((math.pi * 2) ** 0.5) - math.exp(-((i*100/p) ** 2) / 2) > 0:
        print('NO')
print('YES')
