class Solution(object):
    def findRestaurant(self, list1, list2):
        idx_map = {word: i for i, word in enumerate(list1)}
        min_sum = float('inf')
        res = []
        for j, word in enumerate(list2):
            if word in idx_map:
                total = j + idx_map[word]
                if total < min_sum:
                    min_sum = total
                    res = [word]
                elif total == min_sum:
                    res.append(word)
        return res
       
        