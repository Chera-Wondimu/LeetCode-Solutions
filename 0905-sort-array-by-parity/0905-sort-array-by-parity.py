class Solution(object):
    def sortArrayByParity(self, nums):
        for i in range(1, len(nums)):
            j = i
            while j > 0 and nums[j] % 2 == 0 and nums[j - 1] % 2 != 0:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
        return nums
   