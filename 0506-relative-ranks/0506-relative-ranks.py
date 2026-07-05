class Solution:
    def findRelativeRanks(self, score):
        arr = sorted(score, reverse=True)
        rank = {}
        for i in range(len(arr)):
            if i == 0:
                rank[arr[i]] = "Gold Medal"
            elif i == 1:
                rank[arr[i]] = "Silver Medal"
            elif i == 2:
                rank[arr[i]] = "Bronze Medal"
            else:
                rank[arr[i]] = str(i + 1)
        ans = []
        for s in score:
            ans.append(rank[s])
        return ans