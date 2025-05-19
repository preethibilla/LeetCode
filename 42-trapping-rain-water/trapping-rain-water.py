class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0 ,len(height)-1
        leftMax, rightMax = height[left], height[right]
        waterTrap = 0
        while left < right:
            if height[left] < height[right]:
                left += 1
                leftMax = max(leftMax,height[left])
                waterTrap += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax,height[right])
                waterTrap += rightMax - height[right]
        return waterTrap



        