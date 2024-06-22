class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        count = 0
        dict = {'a':0,
                'b':0,
                'c':0
                }

        for r in range(len(s)):
            if s[r] in dict:
                dict[s[r]] += 1
            else:
                dict[s[r]] = 1       
            while dict['a']>0 and dict['b']>0 and dict['c']>0:
                count += len(s)-r
                dict[s[l]] -= 1
                l += 1
        return count
        