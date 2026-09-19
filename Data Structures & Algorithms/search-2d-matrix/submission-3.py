class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, down = 0, ROWS - 1
        while top <= down:
            row = (top + down) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                down = row - 1
            else:
                break
        if not (top <= down):
            return False
        
        row = (top + down) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                l = m + 1
            else:
                r = m - 1
        return False

        