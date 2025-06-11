class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []  # sub[i] = smallest possible tail of LIS of length i+1

        for num in nums:
            # Implement binary search manually to find the position to insert/replace
            left, right = 0, len(sub) - 1
            pos = len(sub)  # Default insert position (at the end)

            while left <= right:
                mid = (left + right) // 2
                if sub[mid] >= num:
                    pos = mid
                    right = mid - 1
                else:
                    left = mid + 1

            if pos == len(sub):
                sub.append(num)  # Extend the subsequence
            else:
                sub[pos] = num  # Replace to keep it minimal

        return len(sub)
        