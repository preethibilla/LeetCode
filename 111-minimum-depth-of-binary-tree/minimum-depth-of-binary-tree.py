# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
# Base case: if the root is None, the depth is 0
        if not root:
            return 0
        
        # If left subtree is None, only consider the right subtree
        if not root.left:
            return self.minDepth(root.right) + 1
        
        # If right subtree is None, only consider the left subtree
        if not root.right:
            return self.minDepth(root.left) + 1
        
        # If both subtrees are not None, return the minimum depth of the two subtrees + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
