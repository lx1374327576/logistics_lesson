import random
import matplotlib.pyplot as plt
# 给出参数
a = 15
b = 2

# 给出w的取值范围
w_max = a / b
w_min = 0


# 给出分销商一阶求导后的方程
def L(w, m):
    global a, b
    return a - b * w - 2 * b * m


def sgn(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1


def solve():
    global a, b, w_max, w_min
    delta = 0.001
    w = []
    for i in range(0, 101, 1):
        w.append(i / 100 * (w_max - w_min) + w_min)

    ans_m = []

    now_m = random.random() * w_max
    for i in range(len(w)):
        step = 1
        slow = 0.999
        while abs(L(w[i], now_m)) > delta:
            now_m -= (L(w[i], now_m + delta) - L(w[i], now_m)) / delta * step * sgn(L(w[i], now_m))
            step = step * slow
        ans_m.append(now_m)

    return w, ans_m


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('w')
ax.set_ylabel('m')
ax.set_title('action m(w) picture')
w, m = solve()
plt.plot(w, m)
plt.show()
