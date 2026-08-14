class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = set()
        R, C = len(grid), len(grid[0])

        def valid(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or (r, c) in visited or grid[r][c] == "0":
                return False
            return True
        
        def dfs(r, c):
            if not valid(r, c):
                return
            
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            return
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1" and (r, c) not in visited:
                    res += 1
                    dfs(r, c)
        return res


        