class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}")
            res.append("#")
            res.append(s)
        print("".join(res))
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        c = 0
        while c < len(s):
            r = c
            while s[r] != "#":
                r += 1
            length = int(s[c:r])
            # print(length)
            res.append(s[r+1 : r + 1 + length])
            # print(res)
            c = r + 1 + length
            
        return res
