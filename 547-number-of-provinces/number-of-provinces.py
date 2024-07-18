class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city: int):
            # Mark the city as visited
            visited[city] = True
            # Visit all the cities connected to this city
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)
        
        n = len(isConnected)
        visited = [False] * n  # List to keep track of visited cities
        provinces = 0  # To count the number of provinces
        
        for city in range(n):
            if not visited[city]:
                dfs(city)
                provinces += 1  # Each DFS corresponds to a new province
        
        return provinces
