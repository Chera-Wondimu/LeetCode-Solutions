class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        highest_count = 0
        most_frequent = None
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
            if freq[num] > highest_count:
                highest_count = freq[num]
                most_frequent = num
        return(most_frequent)