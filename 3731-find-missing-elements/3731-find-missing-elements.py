class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mn = min(nums)
        mx = max(nums)
        ans = []
        for x in range(mn , mx +1):
            if x not in nums:
                ans.append(x)
        return ans

        