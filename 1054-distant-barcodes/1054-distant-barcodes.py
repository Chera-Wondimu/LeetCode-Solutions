class Solution:
    def rearrangeBarcodes(self, barcodes: list[int]) -> list[int]:
        count = Counter(barcodes)
        nums = sorted(count, key=count.get, reverse=True)
        ans = [0] * len(barcodes)
        i = 0
        for num in nums:
            for _ in range(count[num]):
                if i >= len(ans):
                    i = 1
                ans[i] = num
                i += 2
        return ans