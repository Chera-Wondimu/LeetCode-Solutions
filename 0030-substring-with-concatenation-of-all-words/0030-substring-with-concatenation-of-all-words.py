from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        k = len(words[0])
        m = len(words)
        target = sorted(words)
        ans = []
        for i in range(len(s) - k * m + 1):
            cur = []
            for j in range(m):
                cur.append(s[i + j * k : i + (j + 1) * k])
            if sorted(cur) == target:
                ans.append(i)
        return ans