class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(); ans = []

        def dfs(s, cur, total):
            if total == target: ans.append(cur[:]); return
            for i in range(s, len(candidates)):
                if i > s and candidates[i] == candidates[i-1]: continue
                if total + candidates[i] > target: break
                dfs(i+1, cur+[candidates[i]], total + candidates[i])

        dfs(0, [], 0)
        return ans
        