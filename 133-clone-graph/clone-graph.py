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
        if not node:
            return None
        
        # Dictionary to save the cloned nodes
        visited = {}
        
        # Initialize the queue with the starting node
        queue = deque([node])
        
        # Clone the root node and put it in the visited dictionary
        visited[node] = Node(node.val)
        
        while queue:
            curr_node = queue.popleft()
            
            # Iterate through all the neighbors of the current node
            for neighbor in curr_node.neighbors:
                if neighbor not in visited:
                    # Clone the neighbor and put it in the visited dictionary
                    visited[neighbor] = Node(neighbor.val)
                    # Enqueue the neighbor for further traversal
                    queue.append(neighbor)
                    
                # Add the cloned neighbor to the current node's clone's neighbors list
                visited[curr_node].neighbors.append(visited[neighbor])
        
        # Return the clone of the starting node
        return visited[node]
        