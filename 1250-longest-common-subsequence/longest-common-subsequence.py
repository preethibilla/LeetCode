class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        
        # Initialize 2D DP table with (m+1) x (n+1) filled with 0s
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Build the table from top-left to bottom-right
        for i in range(1, m + 1):          # Loop over characters in text1
            for j in range(1, n + 1):      # Loop over characters in text2
                if text1[i - 1] == text2[j - 1]:
                    # If characters match, extend LCS by 1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # Else take max of excluding one character from either string
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Final answer is in the bottom-right cell
        return dp[m][n]


        