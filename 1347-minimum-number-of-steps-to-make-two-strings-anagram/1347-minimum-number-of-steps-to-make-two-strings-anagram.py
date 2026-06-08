class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        count_s = Counter(s)
        count_t = Counter(t)
        steps = 0
        for ch in count_t:
            if count_t[ch] > count_s[ch]:
                steps += count_t[ch] - count_s[ch]

        return steps