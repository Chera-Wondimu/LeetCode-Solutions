class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        target = nums[n//2]
        operations = 0
        for x in nums:
            operations += abs(x - target)
        return(operations)