class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 1D DP array with all 1s
        # There's only 1 way to reach any cell in the first row
        dp = [1] * n

        # Start filling the array row by row (from row 1 to m-1)
        for i in range(1, m):
            for j in range(1, n):
                # dp[j] holds paths from above, dp[j - 1] holds paths from left
                dp[j] += dp[j - 1]

        # The last element contains the result for bottom-right cell
        return dp[-1]

        