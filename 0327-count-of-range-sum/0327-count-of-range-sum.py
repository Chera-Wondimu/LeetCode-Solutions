class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        pre = [0]
        for x in nums:
            pre.append(pre[-1] + x)

        def sort(l, r):
            if r - l <= 1:
                return 0
            m = (l + r) // 2
            ans = sort(l, m) + sort(m, r)
            i = j = m
            for x in pre[l:m]:
                while i < r and pre[i] - x < lower:
                    i += 1
                while j < r and pre[j] - x <= upper:
                    j += 1
                ans += j - i
            pre[l:r] = sorted(pre[l:r])
            return ans
        return sort(0, len(pre))