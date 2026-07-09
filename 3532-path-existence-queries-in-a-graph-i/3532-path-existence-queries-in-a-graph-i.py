class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        arr = [0] * n
        x = 0
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                x += 1
            arr[i] = x
        ans = []
        for u, v in queries:
            ans.append(arr[u] == arr[v])
        return ans
        