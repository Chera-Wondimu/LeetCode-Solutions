class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        arr = []
        for i in range(len(nums)):
            arr.append(nums[i])
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                return True
        return False

        
        


        