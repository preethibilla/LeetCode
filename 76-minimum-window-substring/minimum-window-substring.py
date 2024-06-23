class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        t_count = Counter(t)
        freq = defaultdict(int)
        required = len(t_count)
        formed = 0
        l,r = 0,0
        min_len = float('inf')
        min_left = 0

        while r < len(s):
            freq[s[r]] += 1
            if s[r] in t_count and freq[s[r]] == t_count[s[r]]:
                formed += 1
            while l <= r and formed == required:
                if r-l+1 < min_len:
                    min_len = r-l+1
                    min_left = l
                freq[s[l]] -= 1
                if s[l] in t_count and freq[s[l]] < t_count[s[l]]:
                    formed -= 1
                l += 1
            r += 1
        if min_len == float('inf'):
            return ""
        return s[min_left:min_left+min_len]
        
        


        