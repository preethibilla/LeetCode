"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Base case: if the input node is None, return None
        if not node:
            return None

        # Dictionary to store the visited nodes and their clones
        visited = {}

        # Helper function to perform DFS and clone the graph
        def dfs(node):
            # If the node has already been cloned, return the cloned node
            if node in visited:
                return visited[node]

            # Create a new clone of the node with the same value
            clone_node = Node(node.val)
            # Store the clone in the visited dictionary
            visited[node] = clone_node

            # Recursively clone all neighbors
            for neighbor in node.neighbors:
                # Add the cloned neighbors to the clone_node's neighbors list
                clone_node.neighbors.append(dfs(neighbor))

            # Return the cloned node
            return clone_node

        # Start the DFS from the given node
        return dfs(node)
        