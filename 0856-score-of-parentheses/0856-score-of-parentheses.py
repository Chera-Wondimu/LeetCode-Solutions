class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for c in s :
            if c == "(":
                stack.append(0)
            else:
               x = stack.pop()
               if x == 0:
                 x = 1
               else:
                 x *= 2
               stack[-1] += x
        return stack[0]

