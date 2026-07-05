class Solution :
    def findDuplicates(self, nums):
        ans = []
        for x in nums:
            if x < 0:
                x = -x
            i = x - 1
            if nums[i] < 0:
                ans.append(x)
            else:
                nums[i] = -nums[i]
        return ans


        