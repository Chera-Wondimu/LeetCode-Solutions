from collections import Counter

class Solution:
    def majorityElement(self, nums):
        count = Counter(nums)
        for num in count:
            if count[num] > len(nums) // 2:
                return num