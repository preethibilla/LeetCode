class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
         # Initialize two variables to store the maximum sums
        # max_sum will hold the overall maximum subarray sum found so far
        # current_sum will hold the maximum subarray sum that ends at the current position
        max_sum = nums[0]
        current_sum = nums[0]
        
        # Iterate over the array starting from the second element
        for i in range(1, len(nums)):
            # Update current_sum to be the maximum of the current element alone or the current element added to current_sum
            # This decides whether to start a new subarray at the current element or to continue the existing subarray
            current_sum = max(nums[i], current_sum + nums[i])
            
            # Update max_sum to be the maximum of itself and current_sum
            # This ensures that max_sum always holds the maximum subarray sum found so far
            max_sum = max(max_sum, current_sum)
        
        # Return the overall maximum subarray sum
        return max_sum

        