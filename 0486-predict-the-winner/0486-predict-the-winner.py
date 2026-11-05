class Solution:
    def predictTheWinner(self, nums):
        chera = {}
        def solve(i, j):
            if i == j:
                return nums[i]
            if (i, j) in chera:
                return chera[(i, j)]
            left = nums[i] - solve(i + 1, j)
            right = nums[j] - solve(i, j - 1)
            chera[(i, j)] = max(left, right)
            return chera[(i, j)]
        return solve(0, len(nums) - 1) >= 0