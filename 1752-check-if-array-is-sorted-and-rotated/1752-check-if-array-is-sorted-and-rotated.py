class Solution:
    def check(self, nums: List[int]) -> bool:
        arr = sorted(nums)
        n = len(nums)
        for i in range(n):
            rotated = arr[i:] + arr[:i]
            if rotated == nums:
                return True
        return False