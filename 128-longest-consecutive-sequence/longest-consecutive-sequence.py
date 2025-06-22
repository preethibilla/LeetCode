class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Step 1: Use a set for O(1) access to elements
        numSet = set(nums)

        # Step 2: Variable to track the max sequence length
        longest = 0

        # Step 3: Iterate over each unique number
        for num in numSet:
            # Only try to build a sequence from the start of a streak
            if (num - 1) not in numSet:
                # This is a new streak starter
                length = 1  # Start length count

                # Step 4: Count upward as long as next numbers are in set
                while (num + length) in numSet:
                    length += 1

                # Step 5: Update max streak length found so far
                longest = max(longest, length)

        return longest

        