# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root,1)])
        while queue:
            current, depth = queue.popleft()
            if not current.left and not current.right:
                return depth
            if current.left:
                queue.append((current.left,depth+1))
            if current.right:
                queue.append((current.right,depth+1))
        return 0
        