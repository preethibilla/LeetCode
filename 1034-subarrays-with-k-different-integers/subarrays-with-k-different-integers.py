class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(S):
            l = 0
            d = {}
            count = 0
            for r in range(len(nums)):
                if nums[r] in d:
                    d[nums[r]] += 1
                else:
                    d[nums[r]] = 1
                while len(d) > S:
                    d[nums[l]] -= 1
                    if d[nums[l]] == 0:
                        del d[nums[l]]
                    l += 1
                count += r - l + 1
            return count
        return atMost(k) - atMost(k-1)


        