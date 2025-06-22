class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # This list will store the smallest possible tail of all increasing subsequences
        # of different lengths. The length of this list is the length of LIS.
        sub = []

        for num in nums:
            # Binary search to find the index in 'sub' where 'num' should go
            left, right = 0, len(sub) - 1
            pos = len(sub)  # Default position to append if 'num' is the largest

            while left <= right:
                mid = (left + right) // 2

                if sub[mid] >= num:
                    # If current mid element is >= num, this could be a valid position
                    # but we continue to search on the left to find the earliest
                    pos = mid
                    right = mid - 1
                else:
                    # If current mid element is < num, move right to find larger ones
                    left = mid + 1

            # If 'pos' is equal to length of sub, num is larger than all elements
            # and can extend the LIS by one element
            if pos == len(sub):
                sub.append(num)
            else:
                # Otherwise, replace the element at index 'pos' to maintain the
                # smallest possible tail value for subsequences of this length
                sub[pos] = num

        # Length of the 'sub' array represents the length of LIS
        return len(sub)

        