class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        left = 1
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            count = 0
            for x in nums:
                if x <= mid:
                    count += 1
            if count > mid:
                right = mid
            else:
                left = mid + 1
        return left
            
             
