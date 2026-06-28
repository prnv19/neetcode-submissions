class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        def valid(r, c):
            if r >= 0 and r < R and c >=0 and c < C:
                return True
            return False
        path = set()
        def dfs(r, c, i):
            if i == len(word):
                return True
            if not valid(r, c) or board[r][c] != word[i] or (r, c) in path:
                return False
            path.add((r, c))
            found =  (dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return found    
        for i in range(R):
            for j in range(C):
                if dfs(i, j, 0):
                    return True
        return False
        