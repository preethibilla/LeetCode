class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #keep track of longest streak
        longest_length = 0
        num_set = set(nums)
        #loop through each number in set
        for num in num_set:
            #if the current num has no prev number,then its the start of sequence
            if num-1 not in num_set:
                current_num = num + 1
                current_length = 1
                #continue to check for next consecutive num
                while current_num in num_set:
                    current_num += 1
                    current_length += 1
                #update the longest length if current length is longer
                longest_length = max(longest_length,current_length)
        return longest_length
        