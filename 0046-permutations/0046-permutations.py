class Solution:
    def permute(self, nums):
        result = []

        def backtrack(path):
            if len(path) == len(nums):
                result.append(path.copy())
                return

            for x in nums:
                if x not in path:
                    path.append(x)
                    backtrack(path)
                    path.pop()

        backtrack([])

        return result