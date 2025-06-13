class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        # Count how many islands are in the current grid
        def count_islands():
            visited = set()  
            islands = 0        
            for r in range(len(grid)):  
                for c in range(len(grid[0])):
                    if grid[r][c] == 1 and (r,c) not in visited:
                        self.explore_size(grid, r, c, visited)  
                        islands += 1
                        if islands > 1:
                            return islands # Early exit: more than one island
            return islands
        # Check if the grid is already disconnected
        if count_islands() != 1:
            return 0

        # Try removing each land cell and check if island splits
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    grid[r][c] = 0  # Temporarily remove land
                    if count_islands() != 1:
                        grid[r][c] = 1  # Restore cell
                        return 1  # Only one day needed to disconnect
                    grid[r][c] = 1  # Restore cell after check

        return 2  # If nothing works, we need at least 2 days
    # DFS function to mark all land connected to (r, c)
    def explore_size(self, grid, r, c, visited):
        row_inbounds = 0 <= r < len(grid)  # Check if the current row is within grid bounds
        col_inbounds = 0 <= c < len(grid[0])  # Check if the current column is within grid bounds
        if not row_inbounds or not col_inbounds:
            return 0
        if grid[r][c] == 0:  # Check if the current cell is water
            return 0
        pos = (r, c)  # Create a tuple to represent the current cell's position
        if pos in visited:  # Check if the current cell has already been visited
            return 0
        
        visited.add(pos)  # Mark the current cell as visited
        
        # Recursively explore adjacent cells (up, down, left, right) and add their sizes to the current island size
        self.explore_size(grid, r-1, c, visited)
        self.explore_size(grid, r+1, c, visited)
        self.explore_size(grid, r, c-1, visited)
        self.explore_size(grid, r, c+1, visited)
        
        