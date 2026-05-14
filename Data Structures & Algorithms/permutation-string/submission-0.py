class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}
        for char in s1:
            s1_count[char] = 1 + s1_count.get(char, 0)

        s2_count = {}
        l = 0
        
        for r in range(len(s2)):
            # Add the current character to the window
            char_r = s2[r]
            s2_count[char_r] = 1 + s2_count.get(char_r, 0)

            # If window is too big, remove the leftmost character
            if (r - l + 1) > len(s1):
                char_l = s2[l]
                s2_count[char_l] -= 1
                if s2_count[char_l] == 0:
                    del s2_count[char_l]
                l += 1

            # Compare the maps
            if s1_count == s2_count:
                return True

        return False


        
