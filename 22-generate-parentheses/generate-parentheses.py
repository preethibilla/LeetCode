class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(curr, open_count, close_count):
            # If the current string has reached the maximum length
            if len(curr) == 2 * n:
                result.append(curr)
                return
            
            # If we can still add an opening bracket, do so
            if open_count < n:
                backtrack(curr + '(', open_count + 1, close_count)
            
            # If we can add a closing bracket (i.e., close a previously opened bracket), do so
            if close_count < open_count:
                backtrack(curr + ')', open_count, close_count + 1)
        
        result = []
        backtrack('', 0, 0)
        return result
            