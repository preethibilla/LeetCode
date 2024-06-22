class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        left = k-1
        right = n-1
        currentPoints = 0

        for i in range(k):
            currentPoints += cardPoints[i]
        
        maxPoints = currentPoints

        for _ in range(k):
            currentPoints += cardPoints[right] - cardPoints[left]
            maxPoints = max(maxPoints,currentPoints)
            left -= 1
            right -= 1
        return maxPoints
 

        
