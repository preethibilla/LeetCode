class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        # Initialize the parent and rank arrays for Union-Find
        parent = [i for i in range(n)]
        rank = [0] * n

        # Helper function to find the root of a node with path compression
        def find(x):
            if parent[x] != x:
                # Path compression: make the nodes point directly to the root
                parent[x] = find(parent[x])
            return parent[x]

        # Helper function to union two subsets with union by rank
        def union(x, y):
            xroot, yroot = find(x), find(y)
            if xroot != yroot:
                # Union by rank: attach the shorter tree under the root of the taller tree
                if rank[xroot] > rank[yroot]:
                    parent[yroot] = xroot
                else:
                    parent[xroot] = yroot
                    # If ranks are the same, increment the rank of the new root
                    if rank[xroot] == rank[yroot]:
                        rank[yroot] += 1

        # Iterate over each edge in the input
        for edge in edges:
            a, b = edge[0] - 1, edge[1] - 1  # Convert to zero-based index
            if find(a) == find(b):
                # If both nodes have the same root, an edge forms a cycle
                return edge
            else:
                # Union the two nodes
                union(a, b)

        return None
        