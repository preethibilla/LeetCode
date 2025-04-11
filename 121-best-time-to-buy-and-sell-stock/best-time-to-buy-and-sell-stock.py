class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[l] <= prices[r]:
                max_profit = max(max_profit,prices[r]-prices[l])
            else:
                l = r
            r += 1
        return max_profit

        