class Solution:
    def arrayNesting(self, nums):
        vis = set()
        ans = 0
        for i in range(len(nums)):
            if i not in vis:
                j = i
                cnt = 0
                while j not in vis:
                    vis.add(j)
                    j = nums[j]
                    cnt += 1
                ans = max(ans, cnt)
        return ans