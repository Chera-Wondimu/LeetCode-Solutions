class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for customer in accounts:
            wealth = 0
            for money in customer:
                wealth += money
            if wealth > richest:
                richest = wealth
        return richest
        
        