# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        right_Side = []
        queue = [root]
        while queue:
            level_length = len(queue)
            for i in range(level_length):
                current = queue.pop(0)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)  
                if i == level_length-1:
                    right_Side.append(current.val)  
        return right_Side 