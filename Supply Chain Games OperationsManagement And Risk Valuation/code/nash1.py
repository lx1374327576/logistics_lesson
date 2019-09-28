import random
# 参数
alpha = 0.5
a = 15
b = 2
c = 1


# 方程
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
    global alpha, a, b, c
    ans = []
    delta = 0.001
    for i in range(100):
        step = 1
        slow = 0.99
        p_max = (a / b) ** (1 / alpha)
        w = random.random() * p_max
        m = random.random() * (p_max - w)
        while L1(w, m) <= 0 or L2(w, m) <= 0:
            w = random.random() * p_max
            m = random.random() * (p_max - w)
        now = 0
        while step > 0.000001:
            now += 1
            dw1 = (L1(w + delta, m) - L1(w, m)) / delta
            w -= dw1 * step * sgn(L1(w, m))
            dw2 = (L2(w + delta, m) - L2(w, m)) / delta
            w -= dw2 * step * sgn(L2(w, m))
            dm1 = (L1(w, m + delta) - L1(w, m)) / delta
            m -= dm1 * step * sgn(L1(w, m))
            dm2 = (L2(w, m + delta) - L2(w, m)) / delta
            m -= dm2 * step * sgn(L2(w, m))
            step = step * slow
            # if now % 10 == 0:
            #     print(now, ':')
            #     print(w, m)
            #     print(L1(w, m), L2(w, m))
        if L1(w, m) < delta and L2(w, m) < delta:
            ans.append((w, m))
    if len(ans) == 0:
        return ans
    ans.sort(key=lambda s: (s[0], s[1]))
    ans_tmp = list()
    ans_tmp.append(ans[0])
    for i in range(1, len(ans), 1):
        if abs(ans[i][0] - ans[i - 1][0]) < delta and abs(ans[i][1] - ans[i - 1][1]) < delta:
            continue
        ans_tmp.append(ans[i])
    return ans_tmp


wm = solve()
for i in range(len(wm)):
    print('m = ' + str(wm[i][1]) + '; w = ' + str(wm[i][0]))
