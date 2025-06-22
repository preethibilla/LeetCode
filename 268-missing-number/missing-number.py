class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)  # There should be n+1 numbers in total
        expected_sum = n * (n + 1) // 2  # Sum from 0 to n
        actual_sum = sum(nums)          # Sum of given array
        return expected_sum - actual_sum  # The missing number

        