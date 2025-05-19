class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        maxLen = 0
        count = {}
        for r in range(len(fruits)):
            # if fruits[r] in count:
            #     count[fruits[r]] += 1
            # else:
            #     count[fruits[r]] = 1
            count[fruits[r]] = count.get(fruits[r],0)+1
            while len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1
            maxLen = max(maxLen, r-l+1)
        return maxLen


