class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans = 0
        mx = 0
        for l, r in intervals:
            if r > mx:
                ans += 1
                mx = r
        return ans