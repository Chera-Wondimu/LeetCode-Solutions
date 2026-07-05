class Solution:
    def topKFrequent(self, words, k):
        freq = {}
        for w in words:
            freq[w] = freq.get(w, 0) + 1
        arr = []
        for w in freq:
            arr.append((-freq[w], w))
        arr.sort()
        ans = []
        for i in range(k):
            ans.append(arr[i][1])
        return ans
        