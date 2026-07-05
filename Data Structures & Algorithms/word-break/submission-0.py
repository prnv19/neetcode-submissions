class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                l = len(w)
                # print(w)
                # print(s[i : i + l - 1])
                if i + l - 1 < len(s) and s[i : i + l] == w and dp[i + l]:
                    dp[i] = True
                    # print(dp)
        return dp[0]
        



        
        