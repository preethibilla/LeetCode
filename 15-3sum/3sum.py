class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums)-1
            while l < r:
                Sum = nums[i] + nums[l] + nums[r]
                if Sum < 0:
                    l += 1
                elif Sum > 0:
                    r -= 1
                else: 
                    result.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return result

                
        