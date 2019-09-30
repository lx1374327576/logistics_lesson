import random
import matplotlib.pyplot as plt
# 给出参数
alpha = 0.5
a = 15
b = 2
c = 1

# 给出w的取值范围
w_max = (a / b) ** (1 / alpha)
w_min = 0


# 给出偏导方程
def L1(w, m):
    global alpha, a, b, c
    return a - b * ((w + m) ** alpha) - m * alpha * ((w + m) ** (alpha - 1))


def L2(w, m):
    global alpha, a, b, c
    return a - b * ((w + m) ** alpha) - (w - c) * alpha * ((w + m) ** (alpha - 1))


def sgn(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1


def solve():
    global alpha, a, b, c, w_max, w_min
    delta = 0.001
    w = []
    for i in range(0, 101, 1):
        w.append(i / 100 * (w_max - w_min) + w_min)

    ans1_m = []

    now_m = random.random() * w_max
    for i in range(len(w)):
        step = 1
        slow = 0.999
        while abs(L1(w[i], now_m)) > delta:
            now_m -= (L1(w[i], now_m + delta) - L1(w[i], now_m)) / delta * step * sgn(L1(w[i], now_m))
            step = step * slow
        ans1_m.append(now_m)

    ans2_m = []

    now_m = random.random() * w_max
    for i in range(len(w)):
        step = 1
        slow = 0.999
        while abs(L2(w[i], now_m)) > delta:
            now_m -= (L2(w[i], now_m + delta) - L2(w[i], now_m)) / delta * step * sgn(L2(w[i], now_m))
            step = step * slow
        ans2_m.append(now_m)

    return w, ans1_m, ans2_m


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('w')
ax.set_ylabel('m')
ax.set_title('w-m picture')
w, m1, m2 = solve()
plt.plot(w, m1, label='supplier')
plt.plot(w, m2, label='retailer')
plt.legend()
plt.show()
