# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total_tilt = 0

        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            # Tilt of this node
            tilt = abs(left_sum - right_sum)

            # Add to total tilt
            self.total_tilt += tilt

            # Return total sum including this node
            return left_sum + right_sum + node.val

        dfs(root)
        return self.total_tilt
        