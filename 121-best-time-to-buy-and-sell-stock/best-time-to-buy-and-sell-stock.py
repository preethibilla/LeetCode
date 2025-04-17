class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 0
        max_profit = 0
        
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                max_profit = max(max_profit, prices[right] - prices[left])
            right += 1
        
        return max_profit