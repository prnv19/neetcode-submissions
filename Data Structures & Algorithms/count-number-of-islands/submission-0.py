class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        def valid(r, c):
            if r >= 0 and r < R and c >= 0 and c < C:
                return True
            return False
        
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        res = 0

        def dfs(r, c):
            nonlocal res
            if not valid(r, c) or (r, c) in visited:
                return
            
            if grid[r][c] == "1":
                res += 1
                visited.add((r, c))
                q = deque([[r, c]])
                while q:
                    curr_r, curr_c = q.popleft()
                    for dr, dc in dirs:
                        new_r, new_c = curr_r + dr, curr_c + dc
                        if (valid(new_r, new_c) and (new_r, new_c) not in visited and grid[new_r][new_c] == "1"):
                            q.append([new_r, new_c])
                            visited.add((new_r, new_c))
            return

        for r in range(R):
            for c in range(C):
                if (r, c) not in visited:
                    dfs(r, c)
        return res

        