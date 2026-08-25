class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        ans = 0
        freq = {0:1}
        for x in nums:
            prefix += x
            if prefix - k in freq:
                ans += freq[prefix-k]
            freq[prefix] = freq.get(prefix,0)+1
        return ans
        