class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(S):
            if S < 0:
                return 0      
            l = 0
            sum_window = 0
            count = 0
            for r in range(len(nums)):
                sum_window += nums[r]
                while sum_window > S:
                    sum_window -= nums[l]
                    l += 1
                count += r - l + 1
            return count
        return atMost(goal)-atMost(goal-1)
