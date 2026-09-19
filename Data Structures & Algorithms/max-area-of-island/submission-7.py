class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        res = 0

        def dfs(r, c):
            if (not 0 <= r < ROWS or
                not 0 <= c < COLS or
                (r, c) in visited or
                grid[r][c] == 0):
                return 0
            
            visited.add((r, c))
            area = 1 + (dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c - 1) +
                        dfs(r, c + 1))
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        return res
        