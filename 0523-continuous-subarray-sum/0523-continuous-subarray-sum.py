class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0: -1}
        prefix = 0
        for i, x in enumerate(nums):
            prefix += x
            r = prefix % k
            if r in remainder:
                if i - remainder[r] >= 2:
                    return True
            else:
                remainder[r] = i
        return False
        