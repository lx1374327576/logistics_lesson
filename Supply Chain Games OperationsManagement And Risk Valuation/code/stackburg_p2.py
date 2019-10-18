import random
import matplotlib.pyplot as plt
import math
# 给出参数
a = 15
b = 0.1
c = 1

# 给出x的取值范围
x_max = 10
x_min = 0


# 给出方程
def L(x):
    global a, b, c
    return a * math.e ** (-2 * b * x) - c - x * a * b * math.e ** (-2 * b * x)


def sgn(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1


def solve():
    global a, b, c, x_min, x_max
    delta = 0.001
    w = []
    for i in range(0, 101, 1):
        w.append(i / 100 * (x_max - x_min) + x_min)

    ans_m = []
    for i in range(len(w)):
        ans_m.append(L(w[i]))

    return w, ans_m


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('x')
ax.set_ylabel('L(x)')
ax.set_title('value L(x) picture')
w, m = solve()
plt.plot(w, m)
plt.plot([0] * 10, 'r--')
now = []
for i in range(16):
    now.append(i)
plt.plot([0] * 16, now, 'r--')
plt.show()
