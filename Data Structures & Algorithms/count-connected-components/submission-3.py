class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i : [] for i in range(n)}
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        # print(adj)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for dest in adj[node]:
                dfs(dest)
            return True
        
        res = 0
        for i in range(n):
            if dfs(i):
                res += 1
        return res




            
            
        