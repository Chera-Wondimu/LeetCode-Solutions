class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
           num += 1 << 32
        s = "0123456789abcdef"
        ans = ""
        while num:
          ans = s[num % 16] + ans
          num //= 16
        return ans
        