class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        arr = []
        for i in range(len(nums)):
            arr.append((nums[i], i))
        arr.sort()
        largest = arr[-1][0]
        second = arr[-2][0]
        if largest >= 2 * second:
            return arr[-1][1]
        return -1

