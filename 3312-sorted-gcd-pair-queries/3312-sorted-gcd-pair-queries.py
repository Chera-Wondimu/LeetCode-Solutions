from bisect import bisect_left
class Solution:
    def gcdValues(self, nums, queries):
        m = max(nums)
        freq = [0] * (m + 1)
        for x in nums:
            freq[x] += 1
        div = [0] * (m + 1)
        for i in range(1, m + 1):
            for j in range(i, m + 1, i):
                div[i] += freq[j]
        exact = [0] * (m + 1)
        for i in range(m, 0, -1):
            exact[i] = div[i] * (div[i] - 1) // 2
            for j in range(i * 2, m + 1, i):
                exact[i] -= exact[j]
        pref = []
        vals = []
        s = 0

        for g in range(1, m + 1):
            if exact[g]:
                s += exact[g]
                pref.append(s)
                vals.append(g)

        return [vals[bisect_left(pref, q + 1)] for q in queries]