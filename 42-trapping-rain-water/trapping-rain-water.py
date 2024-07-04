class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        water_trapped = 0
        high = 0
        while l < r:
                low = min(height[l],height[r])
                high = max(high, low)
                water_trapped += high - low
                if height[l] < height[r]:
                    l += 1
                else:
                    r -= 1
        return water_trapped

        