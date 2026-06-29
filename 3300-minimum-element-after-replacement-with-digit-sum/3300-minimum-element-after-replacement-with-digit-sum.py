class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = float("inf")
        for num in nums:
            s = 0
            while num:
                s += num % 10
                num //= 10
            ans = min(ans, s)
        return ans










        