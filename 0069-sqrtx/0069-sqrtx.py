class Solution(object):
    def mySqrt(self, x):
        left, right = 1, x
        while left <= right:
            mid = (right + left)//2
            if mid <= x//mid:
                left = mid + 1
            else:
                right = mid - 1
        return right
