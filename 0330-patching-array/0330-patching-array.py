class Solution(object):
    def minPatches(self, nums, n):
        m = 1
        i = 0
        patches = 0
        while m <= n:
            if i < len(nums) and nums[i] <= m:
                m += nums[i]
                i += 1
            else:
                m += m
                patches += 1
        return patches



        