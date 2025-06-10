class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        def explore(grid, r, c, visited):
            row_inbounds = 0 <= r < len(grid)
            col_inbounds = 0 <= c < len(grid[0])
            if not row_inbounds or not col_inbounds:
                return False
            
            if grid[r][c] == '0':
                return False
            
            pos = (r, c)
            if pos in visited:
                return False
            visited.add(pos)
            
            explore(grid, r - 1, c, visited)
            explore(grid, r + 1, c, visited)  
            explore(grid, r, c - 1, visited)
            explore(grid, r, c + 1, visited)
            
            return True
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if explore(grid, r, c, visited) == True:
                    count += 1
        return count
        