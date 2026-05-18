class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()
        while True:
            ss = 0
            for n in str(n):
                ss += int(n) * int(n)
            if ss == 1:
                return True
            elif ss in hashset:
                return False
            else:
                hashset.add(ss)
                n = ss

                


        