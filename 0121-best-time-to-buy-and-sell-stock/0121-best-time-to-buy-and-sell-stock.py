class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = prices[0]
        Mp = 0
        for price in prices:
            if price < mp:
                mp = price
            else:
                Mp = max(Mp, price - mp)
        return Mp

        