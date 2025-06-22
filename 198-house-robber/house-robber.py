class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]

        # dp[i] = max money that can be robbed from house i to end
        dp = [0] * n
        dp[-1] = nums[-1]                  # Base case: only one house
        dp[-2] = max(nums[-1], nums[-2])   # Base: choose better of last two

        for i in range(n - 3, -1, -1):
            # Either rob current + dp[i+2] or skip to dp[i+1]
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])

        return dp[0]

        