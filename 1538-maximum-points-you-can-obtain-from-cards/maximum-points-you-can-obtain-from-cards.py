class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        if k >= len(cardPoints):
            return total
        curr_Points = 0
        max_Points = 0
        left = 0
        for right in range(len(cardPoints)):
            curr_Points += cardPoints[right]
            if right-left+1 == len(cardPoints)-k:
                max_Points = max(total-curr_Points,max_Points)
                curr_Points -= cardPoints[left]
                left += 1
        return max_Points

 

        
