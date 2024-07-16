class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_size = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                size = self.explore_size(grid,r,c,visited)
                if size > max_size:
                    max_size = size
        return max_size

    def explore_size(self,grid,r,c,visited):
        row_inbounds = 0 <= r < len(grid)
        col_inbounds = 0 <= c < len(grid[0])
        if not row_inbounds or not col_inbounds:
            return 0
        if grid[r][c] == 0:
            return 0
        pos = (r,c)
        if pos in visited:
            return 0
        visited.add(pos)
        size = 1
        size += self.explore_size(grid,r-1,c,visited)
        size += self.explore_size(grid,r+1,c,visited)
        size += self.explore_size(grid,r,c-1,visited)
        size += self.explore_size(grid,r,c+1,visited)
        return size
        