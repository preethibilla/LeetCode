class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        maxLen = 0

        for r in range(len(s)):
            # if s[r] in count:
            #     count[s[r]] += 1
            # else:
            #     count[s[r]] = 1
            count[s[r]] = count.get(s[r],0)+ 1
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            maxLen = max(maxLen,r-l+1)
        return maxLen


        