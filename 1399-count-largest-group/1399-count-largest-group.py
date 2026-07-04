from collections import Counter
class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = Counter()
        for num in range(1, n + 1):
            digit_sum = 0
            x = num
            while x:
                digit_sum += x % 10
                x //= 10
            groups[digit_sum] += 1
        largest = max(groups.values())
        ans = 0
        for size in groups.values():
            if size == largest:
                ans += 1
        return ans