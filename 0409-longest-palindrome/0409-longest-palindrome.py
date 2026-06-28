from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        length = 0
        odd = False
        for freq in count.values():
            if freq % 2 == 0:
                length += freq
            else:
                length += freq - 1
                odd = True
        if odd:
            length += 1
        return length
        