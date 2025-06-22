class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            n = n & (n - 1)  # Remove the rightmost 1 bit
            count += 1       # Count how many times we do this
        return count

        