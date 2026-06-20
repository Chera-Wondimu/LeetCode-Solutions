class Solution(object):
    def nthUglyNumber(self, n):
        u = [1] * n
        a = b = c = 0
        for i in range(1, n):
            u[i] = x = min(u[a]*2, u[b]*3, u[c]*5)
            if x == u[a]*2: a += 1
            if x == u[b]*3: b += 1
            if x == u[c]*5: c += 1
        return u[-1]
