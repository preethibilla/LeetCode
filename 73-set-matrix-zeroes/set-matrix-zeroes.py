class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        
        m, n = len(matrix), len(matrix[0])
        rows_to_zero = set()
        cols_to_zero = set()
        
        # First pass to find all zeros
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows_to_zero.add(i)
                    cols_to_zero.add(j)
        
        # Second pass to set rows and columns to zero
        for i in range(m):
            for j in range(n):
                if i in rows_to_zero or j in cols_to_zero:
                    matrix[i][j] = 0



        