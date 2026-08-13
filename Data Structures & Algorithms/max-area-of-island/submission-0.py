class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()
        R, C = len(grid), len(grid[0])

        def valid(r, c):
            if r < 0 or r >= R or c < 0 or c >= C:
                return False
            if (r, c) in visited:
                return False
            if grid[r][c] == 0:
                return False
            return True

        def dfs(r, c, area):
            if not valid(r, c):
                return 0
            
            visited.add((r, c))
            return (1
                + dfs(r + 1, c, 1 + area)
                + dfs(r - 1, c, 1 + area)
                + dfs(r, c + 1, 1 + area)
                + dfs(r, c - 1, 1 + area))
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] not in visited and grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c, 0))
        return max_area




        