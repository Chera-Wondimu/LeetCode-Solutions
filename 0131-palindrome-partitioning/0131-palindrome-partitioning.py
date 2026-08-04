class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(i, path):
            if i == len(s):
                res.append(path)
                return
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    dfs(j, path + [s[i:j]])
        dfs(0, [])
        return res
        