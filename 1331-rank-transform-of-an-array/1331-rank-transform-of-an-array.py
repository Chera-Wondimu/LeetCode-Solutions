class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_nums = sorted(set(arr))
        rank = {}
        for i in range(len(sorted_nums)):
            rank[sorted_nums[i]] = i + 1
        ans = []
        for num in arr:
            ans.append(rank[num])
        return ans

        