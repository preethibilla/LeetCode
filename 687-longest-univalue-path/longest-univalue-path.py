# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.longest = 0  # Tracks the maximum path length

        def dfs(node):
            if not node:
                return 0  # No path from a null node

            # Recurse into left and right subtrees
            left_len = dfs(node.left)
            right_len = dfs(node.right)

            # Track arrows (edges) from this node if values match
            left_arrow = right_arrow = 0

            if node.left and node.left.val == node.val:
                left_arrow = left_len + 1

            if node.right and node.right.val == node.val:
                right_arrow = right_len + 1

            # Update the global longest path if we can join left and right arrows
            self.longest = max(self.longest, left_arrow + right_arrow)

            # Return the longest one-way path from this node
            return max(left_arrow, right_arrow)

        dfs(root)
        return self.longest
        