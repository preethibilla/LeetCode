class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()  # Set to keep track of visited cells
        max_size = 0  # Variable to keep track of the maximum size of an island found
        
        for r in range(len(grid)):  # Iterate over each row in the grid
            for c in range(len(grid[0])):  # Iterate over each column in the grid
                size = self.explore_size(grid, r, c, visited)  # Calculate the size of the island starting from the current cell
                if size > max_size:  # Update max_size if a larger island is found
                    max_size = size
                    
        return max_size  # Return the maximum size of the island found

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
        size = 1  # Initialize the size of the island
        
        # Recursively explore adjacent cells (up, down, left, right) and add their sizes to the current island size
        size += self.explore_size(grid, r-1, c, visited)
        size += self.explore_size(grid, r+1, c, visited)
        size += self.explore_size(grid, r, c-1, visited)
        size += self.explore_size(grid, r, c+1, visited)
        
        return size  # Return the total size of the island
        