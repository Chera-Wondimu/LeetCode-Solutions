class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arr = sorted(nums)
        for i in range(1,len(arr)):
            if arr[i] == arr[i-1]:
                return True
        return False

        
        


        