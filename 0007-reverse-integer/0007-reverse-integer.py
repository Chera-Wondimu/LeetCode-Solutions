class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        s = str(abs(x))
        reversed_s = s[::-1]
        result = sign * int(reversed_s)
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result