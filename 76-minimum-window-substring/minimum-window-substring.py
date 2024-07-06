class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""  # If either s or t is empty, return an empty string
        
        t_count = Counter(t)  # Count frequencies of characters in t
        
        freq = defaultdict(int)  # Dictionary to count characters in the current window of s
        required = len(t_count)  # Number of unique characters in t that need to be in the window
        formed = 0  # Number of unique characters of t that are currently in the window with the required frequency
        
        l, r = 0, 0  # Two pointers for the window
        min_len = float('inf')  # Initialize minimum window length to infinity
        min_left = 0  # Initialize starting index of the minimum window
        
        while r < len(s):
            freq[s[r]] += 1  # Expand the window by adding the current character s[r] to the window
            
            # Check if the current character s[r] is in t and its frequency matches the required frequency
            if s[r] in t_count and freq[s[r]] == t_count[s[r]]:
                formed += 1  # Increment formed count if this character meets the requirement
            
            # Try to contract the window from the left if all characters from t are in the window
            while l <= r and formed == required:
                if r - l + 1 < min_len:
                    min_len = r - l + 1  # Update minimum window length
                    min_left = l  # Update starting index of the minimum window
                
                freq[s[l]] -= 1  # Remove the character at the left pointer l from the window
                
                # Check if removing s[l] caused it to no longer satisfy the required frequency
                if s[l] in t_count and freq[s[l]] < t_count[s[l]]:
                    formed -= 1  # Decrement formed count as s[l] no longer satisfies the requirement
                
                l += 1  # Move the left pointer to the right to try and find a smaller window
            
            r += 1  # Move the right pointer to expand the window
        
        # If no valid window was found, return an empty string
        if min_len == float('inf'):
            return ""
        
        # Return the minimum window substring found
        return s[min_left:min_left + min_len]
        
        


        