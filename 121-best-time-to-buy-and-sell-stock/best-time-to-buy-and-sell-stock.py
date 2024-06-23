class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_Profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit =  prices[r] - prices[l]
                max_Profit = max(profit,max_Profit)
            else:
                l = r
            r += 1
        return max_Profit

        
            

        