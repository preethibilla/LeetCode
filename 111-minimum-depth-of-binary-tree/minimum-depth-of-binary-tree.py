# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
# Handle the edge case of an empty tree
        if not root:
            return 0
        
        # Initialize the queue with the root node and depth 1
        queue = deque([(root, 1)])
        
        while queue:
            # Pop the current node and its depth
            node, depth = queue.popleft()
            
            # Check if the current node is a leaf node
            if not node.left and not node.right:
                return depth
            
            # Add the left child to the queue if it exists
            if node.left:
                queue.append((node.left, depth + 1))
            
            # Add the right child to the queue if it exists
            if node.right:
                queue.append((node.right, depth + 1))
        
        return 0  # This line will never be reached because we always return when a leaf node is found