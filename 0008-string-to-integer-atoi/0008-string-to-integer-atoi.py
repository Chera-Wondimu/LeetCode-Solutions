class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        n = len(s)
        sign = 1
        result = 0

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        while i < n and s[i] == ' ':
            i += 1

        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            result = result * 10 + digit

            if sign * result > INT_MAX:
                return INT_MAX
            if sign * result < INT_MIN:
                return INT_MIN
            i += 1
        return sign * result