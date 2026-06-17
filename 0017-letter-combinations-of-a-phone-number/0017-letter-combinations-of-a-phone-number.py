class Solution(object):
    def letterCombinations(self, d):
        return (lambda m: reduce(lambda r,x: [p+c for p in r for c in m[x]], d, [""]) if d else [])({"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"})