from collections import Counter
from math import factorial

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)
        half = [0] * 26
        mid = ""

        total = 0
        for c, f in freq.items():
            idx = ord(c) - ord('a')
            half[idx] = f // 2
            total += f // 2
            if f % 2:
                mid = c
        ways = factorial(total)
        for x in half:
            ways //= factorial(x)
        if ways < k:
            return ""
        ans = []
        while total:
            for i in range(26):
                if half[i] == 0:
                    continue
                newWays = ways * half[i] // total
                if newWays >= k:
                    ans.append(chr(i + ord('a')))
                    ways = newWays
                    half[i] -= 1
                    total -= 1
                    break
                else:
                    k -= newWays
        left = "".join(ans)
        return left + mid + left[::-1]