class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time_taken(rate):
        # Your code goes here
            time = 0
            for i in range(len(piles)):
                time += (piles[i] + rate - 1) // rate 
            return time

        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if time_taken(mid) > h:
                left = mid + 1
            else:
                right = mid
                
        return left
        