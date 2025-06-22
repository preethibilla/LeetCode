class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0  # Farthest index we can reach so far

        for i, jump in enumerate(nums):
            if i > max_reach:
                # We're at an index that is not reachable
                return False

            # Update the farthest index we can reach
            max_reach = max(max_reach, i + jump)

            # Early exit: if we can reach the end already
            if max_reach >= len(nums) - 1:
                return True

        return True  # Loop completed, we can reach the end

        