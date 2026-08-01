class Solution:
    def predictTheWinner(self, nums):
        n = len(nums)
        memo = [[None] * n for _ in range(n)]
        def dp(left, right):
            if left == right:
                return nums[left]
            if memo[left][right] is not None:
                return memo[left][right]
            take_left = nums[left] - dp(left + 1, right)
            take_right = nums[right] - dp(left, right - 1)
            memo[left][right] = max(take_left, take_right)
            return memo[left][right]
        return dp(0, n - 1) >= 0