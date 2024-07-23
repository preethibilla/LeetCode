class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create an adjacency list for the graph
        adj_list = defaultdict(list)
        in_degree = [0] * numCourses
        
        # Populate the adjacency list and in-degree array
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            in_degree[dest] += 1
        
        # Initialize the queue with nodes that have zero in-degree
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        result = []
        
        while queue:
            node = queue.popleft()
            result.append(node)
            
            # Decrease the in-degree of neighboring nodes
            for neighbor in adj_list[node]:
                in_degree[neighbor] -= 1
                # If in-degree becomes zero, add it to the queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Check if we have included all courses
        if len(result) == numCourses:
            return result
        else:
            return []
        