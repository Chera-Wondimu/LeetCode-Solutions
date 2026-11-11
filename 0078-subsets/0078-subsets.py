class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = [[]]
        for x in nums: 
            arr += [s + [x] for s in arr]
        return arr
        