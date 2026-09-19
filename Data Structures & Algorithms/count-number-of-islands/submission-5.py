class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        res = 0

        def dfs(r, c):
            if (r, c) in visited or not 0 <= r < ROWS or not 0 <= c < COLS or grid[r][c] == "0":
                return
            
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == "1":
                    res += 1
                    dfs(r, c)
        return res
            
        