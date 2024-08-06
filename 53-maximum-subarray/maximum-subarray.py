class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize maxSub to the first element of the array.
        # This will store the maximum subarray sum found so far.
        maxSub = nums[0]
        
        # Initialize curSum to 0.
        # This will store the current subarray sum.
        curSum = 0
        
        # Iterate through each element in the array.
        for n in nums:
            # If curSum is less than 0, reset it to 0.
            # This is because a negative sum will reduce the total sum of any subarray it is part of.
            if curSum < 0:
                curSum = 0
            
            # Add the current element to curSum.
            curSum += n
            
            # Update maxSub to be the maximum of maxSub and curSum.
            # This ensures maxSub always holds the highest subarray sum found so far.
            maxSub = max(curSum, maxSub)
        
        # Return the maximum subarray sum.
        return maxSub

        