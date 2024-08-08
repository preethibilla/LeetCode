class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(current,openbrace_count,closebrace_count):
            nonlocal result
            if len(current) == n*2:
                result.append(current)
                return
            if openbrace_count < n:
                backtrack(current + "(", openbrace_count + 1, closebrace_count)
            if closebrace_count < openbrace_count:
                backtrack(current + ")", openbrace_count, closebrace_count+1)
            return
        result=[]
        backtrack("", 0, 0)
        return result
            