class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Step 1: Initialize DP array with "infinite" values
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins to make amount 0

        # Step 2: Build the DP table
        for coin in coins:
            for x in range(coin, amount + 1):
                # Only update dp[x] if x - coin is valid
                dp[x] = min(dp[x], dp[x - coin] + 1)

        # Step 3: Return result
        return dp[amount] if dp[amount] != float('inf') else -1
