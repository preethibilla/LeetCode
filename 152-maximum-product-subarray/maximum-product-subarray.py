class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curr_max = curr_min = result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            # Swap before updating if num is negative
            if num < 0:
                curr_max, curr_min = curr_min, curr_max

            # Compute new max and min products ending at this index
            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)

            # Update result with the best so far
            result = max(result, curr_max)

        return result
