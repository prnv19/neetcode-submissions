class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                elif grid[r][c] == -1:
                    visited.add((r, c))

        level = 1
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    new_r, new_c = r + dr, c + dc
                    if (0 <= new_r < ROWS and 
                        0 <= new_c < COLS and
                        (new_r, new_c) not in visited and
                        grid[new_r][new_c] == 2147483647):

                        q.append([new_r, new_c])
                        visited.add((new_r, new_c))
                        grid[new_r][new_c] = level
                        
             
            level += 1
        return


        