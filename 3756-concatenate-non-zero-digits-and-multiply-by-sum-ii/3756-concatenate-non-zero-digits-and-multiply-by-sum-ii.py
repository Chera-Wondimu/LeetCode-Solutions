class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        pos = []
        digit = []
        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digit.append(int(ch))
        n = len(digit)
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
        val = [0] * (n + 1)
        sm = [0] * (n + 1)
        for i in range(n):
            val[i + 1] = (val[i] * 10 + digit[i]) % MOD
            sm[i + 1] = sm[i] + digit[i]
        ans = []
        for l, r in queries:
            L = bisect_left(pos, l)
            R = bisect_right(pos, r)
            if L == R:
                ans.append(0)
                continue
            x = (val[R] - val[L] * pow10[R - L]) % MOD
            ssum = sm[R] - sm[L]
            ans.append((x * ssum) % MOD)
        return ans
        