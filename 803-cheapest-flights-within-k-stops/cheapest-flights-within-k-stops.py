class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Step 1: Build the graph
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # Step 2: Use a priority queue to perform a modified Dijkstra's algorithm
        min_heap = [(0, src, 0)]  # (current cost, current city, current number of stops)
        visited = {}

        while min_heap:
            cost, city, stops = heapq.heappop(min_heap)

            # If we've reached the destination with the allowed stops, return the cost
            if city == dst:
                return cost

            # If the number of stops exceeds K, continue
            if stops > k:
                continue

            # Add the current city to visited with the number of stops
            if (city, stops) in visited and visited[(city, stops)] <= cost:
                continue
            visited[(city, stops)] = cost

            # Explore the neighbors
            for neighbor, price in graph[city]:
                new_cost = cost + price
                heapq.heappush(min_heap, (new_cost, neighbor, stops + 1))

        return -1
        