class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_Sum = 0
        left = 0
        curr_Sum = 0
        freq = {}
        for right in range(len(nums)):
            curr_Sum += nums[right]
            freq[nums[right]] = freq.get(nums[right],0)+1
            if right-left+1 == k:
                if len(freq) == k:
                    max_Sum = max(max_Sum,curr_Sum)
                curr_Sum -= nums[left]
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
        return max_Sum

            
        