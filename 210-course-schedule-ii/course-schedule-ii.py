class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Set to keep track of visited nodes
        visited = set()
        # Adjacency list to represent the graph
        adj = [[] for _ in range(numCourses)]
        # Array to determine if a node is a source node (no incoming edges)
        is_source = [True] * numCourses
        # List to store the result (course order)
        solution = []

        def dfs(i: int, stack: Set[int] = set()):
            # Mark the current node as visited
            visited.add(i)
            # Add the current node to the recursion stack
            stack.add(i)
            # Explore all the neighbors (nodes that have a prerequisite of the current node)
            for neighbor in adj[i]:
                if neighbor in visited:
                    # Check for a cycle (if neighbor is in the current recursion stack)
                    if neighbor in stack:
                        return False
                else:
                    # Perform DFS on the unvisited neighbor
                    if not dfs(neighbor, stack):
                        return False
            # Remove the current node from the recursion stack
            stack.remove(i)
            # Add the current node to the solution (post-order traversal)
            solution.append(i)
            return True

        # Build the adjacency list from the prerequisites list
        for prereq in prerequisites:
            pre, post = prereq[1], prereq[0]
            adj[pre].append(post)
            # Mark the node as not a source node (it has incoming edges)
            is_source[post] = False

        # Perform DFS from all source nodes (nodes with no incoming edges)
        for i in range(numCourses):
            if is_source[i]:
                if not dfs(i):
                    # If a cycle is detected, return an empty list
                    return []

        # Ensure all nodes have been visited
        if len(visited) == numCourses:
            # Reverse the solution to get the correct topological order
            solution.reverse()
            return solution
        else:
            # If not all nodes are visited, return an empty list
            return []
            