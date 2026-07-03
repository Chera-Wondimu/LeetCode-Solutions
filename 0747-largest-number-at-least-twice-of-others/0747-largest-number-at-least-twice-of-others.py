class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
       largest = max(nums)
       index = nums.index(largest)
       for i in range(len(nums)):
         if i != index and largest < 2 * nums[i]:
             return -1
       return index


