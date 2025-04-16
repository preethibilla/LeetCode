class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        maxSub = 0
        currSum = 0
        l = 0
        for r in range(len(nums)):
            currSum += nums[r]
            count[nums[r]] += 1
            if r - l + 1 > k:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    count.pop(nums[l])
                currSum -= nums[l]
                l += 1
            if len(count) == k and r - l + 1 == k:
                maxSub = max(currSum,maxSub)
        return maxSub
            
        