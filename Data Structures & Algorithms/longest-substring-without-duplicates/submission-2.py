class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        counts = {}
        res = 0
        while r < len(s):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            while counts[s[r]] > 1:
                counts[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res

        