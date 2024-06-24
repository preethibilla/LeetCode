import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k <= 0:
            return []
        min_heap = []
        for i in range(min(k,len(nums2))):
            heapq.heappush(min_heap,(nums1[0]+nums2[i],0,i))
        result = []
        while min_heap and len(result) < k:
            current_sum,p1,p2=heapq.heappop(min_heap)
            result.append([nums1[p1],nums2[p2]])
            if p1 + 1 < len(nums1):
                heapq.heappush(min_heap,(nums1[p1+1]+nums2[p2],p1+1,p2))
        return result
