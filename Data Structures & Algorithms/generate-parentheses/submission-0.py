class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(cur, openN, closeN):
            if openN == closeN == n:
                res.append("".join(cur.copy()))
            
            if closeN < openN:
                cur.append(")")
                dfs(cur, openN, closeN + 1)
                cur.pop()
            if openN < n:
                cur.append("(")
                dfs(cur, openN + 1, closeN)
                cur.pop()
            
        dfs([], 0, 0)
        return res

        