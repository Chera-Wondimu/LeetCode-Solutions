class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in x:
                return [x[complement], i]
            
            x[num] = i
        