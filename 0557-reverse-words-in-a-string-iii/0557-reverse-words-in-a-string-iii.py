class Solution(object):
    def reverseWords(self, s):
        s = list(s)
        def reverse(l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        start = 0
        for i in range(len(s) + 1):
            if i == len(s) or s[i] == " ":
                reverse(start, i - 1)
                start = i + 1
        return "".join(s)


        