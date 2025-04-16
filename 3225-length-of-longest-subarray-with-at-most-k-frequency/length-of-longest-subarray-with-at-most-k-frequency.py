class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        maxLen = float('-inf')
        count = defaultdict(int)
        l = 0
        for r in range(len(nums)):
            count[nums[r]] += 1
            while count[nums[r]] > k:
                count[nums[l]] -= 1
                l += 1
            maxLen = max(maxLen,r-l+1)
        return maxLen
        