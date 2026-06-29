class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, d = 0 , len(matrix) - 1
        while t <= d:
            row = (t + d) // 2
            if matrix[row][0] <= target <= matrix[row][-1]:
                break
            if target < matrix[row][0]:
                d = row - 1
            else:
                t = row + 1
        
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] == target:
                return True
            if target < matrix[row][m]:
                r = m - 1
            else:
                l = m + 1
        return False
            
        