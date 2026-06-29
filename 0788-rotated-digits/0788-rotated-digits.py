class Solution:
    def rotatedDigits(self, n: int) -> int:
        ans = 0
        for num in range(1, n + 1):
            good = False
            x = num
            while x:
                digit = x % 10
                if digit in (3, 4, 7):
                    break
                if digit in (2, 5, 6, 9):
                    good = True
                x //= 10
            else:
                if good:
                    ans += 1
        return ans
        