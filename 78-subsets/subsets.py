class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start,path):
            # Append the current subset (path) to the result list
            result.append(path)
            # Iterate over the remaining elements starting from 'start'
            for i in range(start,len(nums)):
            # Include nums[i] in the subset and move to the next element
                backtrack(i+1,path+[nums[i]])
        # Start the backtracking with an empty subset
        backtrack(0,[])
        return result