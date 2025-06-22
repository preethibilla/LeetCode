class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)  # Step 1: Initialize output array of size n + 1

        for i in range(1, n + 1):  # Step 2: Loop from 1 to n
            dp[i] = dp[i >> 1] + (i & 1)  # Step 3: Use DP formula

        return dp  # Step 4: Return the filled list

        