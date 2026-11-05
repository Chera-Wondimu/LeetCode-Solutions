class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        def power(x, y):
            if y == 0:
                return 1
            half = power(x, y // 2)
            half = (half * half) % MOD
            if y % 2 == 1:
                half = (half * x) % MOD
            return half
        even = (n + 1) // 2
        odd = n // 2
        return (power(5, even) * power(4, odd)) % MOD