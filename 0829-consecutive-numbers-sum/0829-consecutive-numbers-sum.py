class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ans = 0
        k = 1
        while k * (k + 1) // 2 <= n:
            if (2 * n) % k == 0:
                t = (2 * n) // k - k + 1
                if t > 0 and t % 2 == 0:
                    ans += 1
            k += 1
        return ans