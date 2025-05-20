class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
         # Step 1: Find the sum of the first k numbers
        current_sum = 0
        for i in range(k):
            current_sum += nums[i]

        # Step 2: This is the first possible average
        max_sum = current_sum

        # Step 3: Move the window one number at a time
        for i in range(k, len(nums)):
            # Remove the number that goes out of the window
            current_sum = current_sum - nums[i - k]
            # Add the new number that comes into the window
            current_sum = current_sum + nums[i]
            # Update the max sum if current sum is larger
            if current_sum > max_sum:
                max_sum = current_sum

        # Step 4: Return the average
        return max_sum / k
        