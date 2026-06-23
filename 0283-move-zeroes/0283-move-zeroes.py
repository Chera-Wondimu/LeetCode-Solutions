class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        ph = 0
        for seek in range(len(nums)):
            if nums[seek] !=0:
                nums[seek], nums[ph]= nums[ph],nums[seek]
                ph +=1
        
        