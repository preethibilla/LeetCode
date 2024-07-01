class Solution:
    def __init__(self):
        self.res = dict()

    def uniquePaths(self, m: int, n: int) -> int:
        # Check for out of bound matrix cell
        if m <= 0 or n <= 0:
            return 0
        # There is only one path to reach origin cell of matrix
        if m == 1 and n == 1:
            return 1
        
        # p(m, n) = Number of unique paths to reach cell (m, n) 
        # p(m, n) = p(m-1, n) + p(m, n-1)   Only two ways to move right and down.
        if (m, n) not in self.res:
            self.res[(m, n)] = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        return self.res[(m, n)]

        