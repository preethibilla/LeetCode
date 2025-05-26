# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []  # This will store all valid paths

        def dfs(node, current_path, current_sum):
            if not node:
                return  # Base case: if the node is None, do nothing

            # Add the current node's value to the path and sum
            current_path.append(node.val)
            current_sum += node.val

            # If it's a leaf node and the sum matches, save the path
            if not node.left and not node.right:
                if current_sum == targetSum:
                    # Append a copy of the current path to result
                    result.append(list(current_path))

            # Recurse to the left and right children
            dfs(node.left, current_path, current_sum)
            dfs(node.right, current_path, current_sum)

            # Backtrack: remove the current node before returning
            current_path.pop()

        # Start the DFS from the root
        dfs(root, [], 0)
        return result

        