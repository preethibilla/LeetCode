class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen = set()
        left = 0
        curr_sum = 0
        max_sum = 0

        for right in range(len(nums)):
            # If duplicate found, shrink the window
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

            # Add the current number
            seen.add(nums[right])
            curr_sum += nums[right]

            # Check if window size is exactly k
            if right - left + 1 == k:
                max_sum = max(max_sum, curr_sum)
                # Move left to keep window size k
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

        return max_sum
            
        