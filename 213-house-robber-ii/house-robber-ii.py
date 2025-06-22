class Solution:
    def rob(self, nums: List[int]) -> int:
        # Handle base cases
        if not nums:
            return 0  # No houses

        if len(nums) == 1:
            return nums[0]  # Only one house, rob it

        # rob_linear is the classic House Robber I
        def rob_linear(houses):
            rob1, rob2 = 0, 0
            for amount in houses:
                # Either rob this house + rob1 (skip previous), or skip this house
                temp = max(amount + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        # Case 1: rob houses 0 to n-2
        max1 = rob_linear(nums[:-1])
        # Case 2: rob houses 1 to n-1
        max2 = rob_linear(nums[1:])

        # Return the max of the two cases
        return max(max1, max2)

        