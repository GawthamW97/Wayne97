class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n -1):
            return False

        adj = [[] for _ in range(n)]
        # build a adjacency list since this is indirected graph, we need to consider
        # 1,0 and 0,1
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()   # the visited set has two purpose, one will be to detect cycle,
                        # the other will be to determine if we traveresed the entire tree nodes or not

        def dfs(node,par):
            if node in visit: # if the node is found in the visit set then it's a cycle
                return False

            visit.add(node)
            for nei in adj[node]: # iterate through the adjacency list
                if nei == par:  # if the parent and the the neigbour are same then continue to next element
                    continue
                if not dfs(nei, node): # if not recursively visit, by making the current node as the parent
                    return False
            return True
        return dfs(0,-1) and len(visit) == n # if no cycle exists in the component containing node 0 and every node is connected to node 0

