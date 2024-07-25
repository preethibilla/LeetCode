class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Step 1: Build the graph using adjacency list
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))
        
        # Step 2: Dijkstra's algorithm
        min_heap = [(0, k)]  # (distance, node)
        dist = {}
        
        while min_heap:
            d, node = heapq.heappop(min_heap)
            if node in dist:
                continue
            dist[node] = d
            for neighbor, weight in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(min_heap, (d + weight, neighbor))
        
        # Step 3: If we visited all nodes, return the maximum distance
        if len(dist) == n:
            return max(dist.values())
        else:
            return -1
        