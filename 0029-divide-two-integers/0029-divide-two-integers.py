class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        ans = int(dividend /divisor)
        return(min(max(ans, -2**31), INT_MAX))