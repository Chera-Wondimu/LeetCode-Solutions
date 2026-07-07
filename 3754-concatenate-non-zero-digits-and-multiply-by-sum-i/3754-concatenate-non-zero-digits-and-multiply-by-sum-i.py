class Solution:
    def sumAndMultiply(self, n: int) -> int:
       x = 0
       sum = 0
       for ch in str(n):
          if ch !='0':
            d = int(ch)
            x = x *10 + d
            sum += d
       return x * sum
