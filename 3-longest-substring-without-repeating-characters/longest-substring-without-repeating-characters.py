class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        maxLen = 0
        for right in range(len(s)):
            seen[s[right]]= seen.get(s[right],0)+1
            while seen[s[right]] > 1 :
                seen[s[left]] -= 1
                left += 1
            maxLen = max(maxLen,right-left+1)
        return maxLen


        