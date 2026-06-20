class Solution(object):
    def constructTransformedArray(self, nums):
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[i] = nums[(i + nums[i]) % n]
        return a
        
        
        