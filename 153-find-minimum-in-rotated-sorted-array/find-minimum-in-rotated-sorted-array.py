class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # If middle element is greater than right, min is in right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Otherwise, min is at mid or to the left
                right = mid

        # Left will point to the smallest value
        return nums[left]


        