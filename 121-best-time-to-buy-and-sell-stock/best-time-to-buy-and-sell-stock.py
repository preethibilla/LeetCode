class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_profit = float('inf')
        for price in prices:
            if price < min_profit:
                min_profit = price
            elif price - min_profit > max_profit:
                max_profit = price - min_profit
        return max_profit
        