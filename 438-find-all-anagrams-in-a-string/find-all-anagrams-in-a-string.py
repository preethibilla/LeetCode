class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        p_Count = Counter(p)
        s_Count = Counter(s[:len(p)-1])
        result = []
        for i in range(len(p)-1,len(s)):
            s_Count[s[i]] += 1
            if s_Count == p_Count:
                result.append(i-len(p)+1)
            s_Count[s[i-len(p)+1]] -= 1
            if s_Count[s[i-len(p)+1]] == 0:
                del s_Count[s[i-len(p)+1]]
        return result