class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        watertrap = 0
        high = 0
        while l < r:
            low = min(height[l],height[r])
            high = max(low,high)
            watertrap += high - low
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return watertrap



        