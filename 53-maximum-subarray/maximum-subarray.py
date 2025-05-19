class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = float('-inf')
        currSum = 0
        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSub = max(currSum,maxSub)
        return maxSub

        