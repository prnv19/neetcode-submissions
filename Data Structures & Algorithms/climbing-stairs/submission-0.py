class Solution:
    def climbStairs(self, n: int) -> int:
        x1 = 1
        x2 = 1
        for i in range(n - 1):
            x1, x2 = x2, x1 + x2
        return x2
        