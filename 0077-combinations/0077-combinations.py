class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans = []
        current = []
        def solve(index):
            if len(current) == k:
                ans.append(current.copy())
                return
            for i in range(index, n + 1):
                current.append(i)
                solve(i + 1)
                current.pop()
        solve(1)
        return ans