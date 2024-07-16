class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        colorToReplace = image[sr][sc]
        if colorToReplace == color:
            return image
        def dfs(r,c):
            if (0<=r<rows and 0<=c<cols and image[r][c] == colorToReplace):
                image[r][c] = color
                dfs(r-1,c)
                dfs(r,c-1)
                dfs(r+1,c)
                dfs(r,c+1)
        dfs(sr,sc)
        return image



        