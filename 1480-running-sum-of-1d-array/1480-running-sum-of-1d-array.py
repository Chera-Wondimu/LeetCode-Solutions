class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
      ans = []
      for i in range(len(nums)):
        if i == 0:
            ans.append(nums[i])
        else:
            ans.append(nums[i] + ans[i-1])
      return ans
        