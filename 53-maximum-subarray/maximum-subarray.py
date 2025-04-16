class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
          #intialise the maxSub to the first element of the array.
        maxSub = nums[0]
        #curSum to 0
        curSum = 0
        #iterate through each element in the array.
        for n in nums:
            #if the curSum is less tham 0 , then we reset it to 0(since negative numbers reduce the sum found so far)
            if curSum < 0:
                curSum = 0
            #we add the current element to curSum.
            curSum += n
            #update the maxSub to be the maximum of maxSub and curSub
            maxSub = max(curSum,maxSub)
        return maxSub
        