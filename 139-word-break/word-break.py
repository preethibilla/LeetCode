class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert the word dictionary to a set for faster lookups
        word_set = set(wordDict)
        
        # Initialize a DP array of size len(s) + 1 with all values set to False
        # dp[i] means whether the substring s[:i] can be segmented into words in the dictionary
        dp = [False] * (len(s) + 1)
        
        # Base case: an empty string can always be segmented
        dp[0] = True
        
        # Iterate through the string s
        for i in range(1, len(s) + 1):
            # For each position i, check all possible starting positions j
            for j in range(i):
                # If dp[j] is True and the substring s[j:i] is in the word set
                if dp[j] and s[j:i] in word_set:
                    # Set dp[i] to True and break out of the inner loop
                    dp[i] = True
                    break
        
        # Return dp[len(s)], which indicates if the entire string can be segmented
        return dp[len(s)]
