class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        ans = set(nums[0])
        for arr in nums[1:]:
            ans = ans.intersection(set(arr))
        return(sorted(ans))