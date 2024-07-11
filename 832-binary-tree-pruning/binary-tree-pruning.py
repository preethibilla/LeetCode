# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def prune(node):
            # Base case: If the node is None, return None
            if not node:
                return None
            
            # Recursively prune the left subtree
            node.left = prune(node.left)
            # Recursively prune the right subtree
            node.right = prune(node.right)
            
            # If the current node's value is 0 and it has no left or right subtree, prune it
            if node.val == 0 and not node.left and not node.right:
                return None
            
            # Return the current node after potential pruning of its subtrees
            return node
        
        # Call the helper function with the root of the tree
        return prune(root)



        