class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
                # Edge case: if there are 2 or fewer nodes, return them as the roots of the MHTs
        if n <= 2:
            return [i for i in range(n)]

        # Build the graph with the adjacency list
        # neighbors will be a list of sets, where each set contains the neighbors of the corresponding node
        neighbors = [set() for i in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)

        # Initialize the first layer of leaves
        # leaves will contain all nodes with only one neighbor
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)

        # Number of remaining nodes
        remaining_nodes = n

        # Trim the leaves until reaching the centroids
        while remaining_nodes > 2:
            # Decrease the count of remaining nodes by the number of current leaves
            remaining_nodes -= len(leaves)
            new_leaves = []
            # Remove the current leaves along with the edges
            while leaves:
                leaf = leaves.pop()  # Remove the leaf node
                # The only neighbor left for the leaf node
                neighbor = neighbors[leaf].pop()  # Remove the leaf from its neighbor's set
                # Remove the only edge left
                neighbors[neighbor].remove(leaf)
                # If the neighbor becomes a leaf (i.e., has only one connection left), add it to new_leaves
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)

            # Prepare for the next round of leaf removal
            leaves = new_leaves

        # The remaining nodes are the centroids of the graph and roots of the MHTs
        return leaves
        