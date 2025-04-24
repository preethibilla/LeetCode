class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize two pointers for binary search
        l, r = 0, len(nums) - 1

        # Continue searching while the range is valid
        while l < r:
            # Find the middle index of the current range
            mid = l + (r - l) // 2

            # Case 1: middle element is greater than rightmost
            # This means the smallest element must be to the right of mid
            # Why? Because in a rotated array like [4,5,6,1,2], 6 > 2 => rotation is on the right side
            if nums[mid] > nums[r]:
                l = mid + 1  # Discard the left half including mid

            # Case 2: middle element is less than or equal to rightmost
            # This means the smallest element is at mid or to the left of mid
            # Why? Because this portion is already sorted and may contain the minimum
            else:
                r = mid  # Keep mid in range and discard the right half after mid

        # At the end, l == r and points to the smallest element
        return nums[l]

        