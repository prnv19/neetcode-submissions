class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True
        adj = {i : [] for i in range(n)}
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for nxt in adj[node]:
                if prev == nxt:
                    continue
                if not dfs(nxt, node):
                    return False
            return True
        
        return dfs(0, -1) and (len(visited) == n)
        
        

        