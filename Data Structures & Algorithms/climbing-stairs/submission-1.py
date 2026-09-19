class Solution:
    def climbStairs(self, n: int) -> int:
        x1, x2 = 0, 1
        for _ in range(n):
            x1, x2 = x2, x1 + x2
        return x2
        