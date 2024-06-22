class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        totalsum = sum(cardPoints)

        if k == n:
            return totalsum
        windowsize = n-k
        min_subarray_sum = float('inf')
        currentsum = sum(cardPoints[:windowsize])
        min_subarray_sum = min(min_subarray_sum,currentsum)

        for i in range(windowsize,n):
            currentsum += cardPoints[i] - cardPoints[i-windowsize]
            min_subarray_sum = min(min_subarray_sum,currentsum)
        return totalsum - min_subarray_sum
 

        
