class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert all integers in the list to strings
        str_nums = list(map(str, nums))

        # Custom comparator
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        # Sort using the custom comparator
        str_nums.sort(key=cmp_to_key(compare))

        # Join sorted numbers into a single string
        largest_num = ''.join(str_nums)

        # Edge case: if the largest number is '0', return '0'
        if largest_num[0] == '0':
            return '0'
        else:
            return largest_num
        