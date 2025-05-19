class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currSum = nums[0]
        for i in range(1,len(nums)):
            currSum = max(nums[i],currSum+nums[i])
            maxSub = max(currSum,maxSub)
        return maxSub

        