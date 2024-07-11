class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}
        
        def num_trees(n: int) -> int:
            # Base case: There is one unique BST with 0 or 1 node.
            if n <= 1:
                return 1
            
            # Check if the result is already computed and stored in memo.
            if n in memo:
                return memo[n]
            
            total_trees = 0
            # Compute the number of unique BSTs by choosing each number as root.
            for i in range(1, n + 1):
                left_trees = num_trees(i - 1)
                right_trees = num_trees(n - i)
                total_trees += left_trees * right_trees
            
            # Store the result in memo.
            memo[n] = total_trees
            return total_trees
        
        return num_trees(n)
        