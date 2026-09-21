class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i : set() for i in range(9)}
        cols = {i : set() for i in range(9)}
        squares = {(r, c) : set() for r in range(3) for c in range(3)}

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                num = board[r][c]
                square_r = r // 3
                square_c = c // 3

                if (num in rows[r] or
                    num in cols[c] or
                    num in squares[(square_r, square_c)]):
                    return False
                
                rows[r].add(num)
                cols[c].add(num)
                squares[(square_r, square_c)].add(num)
        return True
