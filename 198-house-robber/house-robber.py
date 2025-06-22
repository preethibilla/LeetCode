class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1 stores the max money robbed up to the house before the previous (i-2)
        # rob2 stores the max money robbed up to the previous house (i-1)
        rob1, rob2 = 0, 0

        # Loop through each house (each value in nums)
        for num in nums:
            # temp stores the max money if we rob this house or skip it
            # If we rob this house: num + rob1 (can't rob previous)
            # If we skip it: rob2 (take the max up to previous)
            temp = max(num + rob1, rob2)

            # Move the rob1 and rob2 pointers forward:
            # rob1 becomes previous rob2
            # rob2 becomes the best value at this step (temp)
            rob1 = rob2
            rob2 = temp

        # After the loop, rob2 contains the max amount that can be robbed
        return rob2

        