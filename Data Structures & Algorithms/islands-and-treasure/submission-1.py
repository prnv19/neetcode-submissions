class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        q = deque([])
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))
                elif grid[r][c] == -1:
                    visited.add((r, c))
        level = 0
        while q:
            level += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    new_r, new_c = r + dr, c + dc
                    if (0 <= new_r < ROWS and 
                        0 <= new_c < COLS and
                        (new_r, new_c) not in visited):
                        grid[new_r][new_c] = level
                        visited.add((new_r, new_c))
                        q.append([new_r, new_c])
