class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            if i == 0:
                ans.append(nums[i])
            else:
                ans.append(nums[i] + ans[i-1])
        return ans
        