class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float('inf')
        left = 0
        currSum = 0
        for right in range(len(nums)):
            currSum += nums[right] #expland the window
            #shrinking the window for the leftside while the currSum is enough.
            while currSum >= target:
                minLen = min(minLen,right-left+1)
                currSum -= nums[left]
                left += 1
        return 0 if minLen == float('inf') else minLen


        