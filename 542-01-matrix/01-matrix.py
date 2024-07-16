class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
         # Get the number of rows and columns in the matrix
        rows, cols = len(mat), len(mat[0])
        
        # Initialize a queue to perform BFS
        queue = deque()
        
        # Iterate through all cells in the matrix
        for r in range(rows):
            for c in range(cols):
                # If the cell contains a 0, add its position to the queue
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    # If the cell contains a 1, set it to infinity to indicate it hasn't been visited
                    mat[r][c] = float('inf')
        
        # Define the four possible directions (right, down, left, up)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Perform BFS
        while queue:
            # Dequeue an element from the front of the queue
            r, c = queue.popleft()
            # Check all four possible directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Ensure the new position is within bounds and hasn't been visited
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] > mat[r][c] + 1:
                    # Update the distance to the nearest 0
                    mat[nr][nc] = mat[r][c] + 1
                    # Enqueue the new position for further exploration
                    queue.append((nr, nc))
        
        # Return the updated matrix with distances to the nearest 0
        return mat