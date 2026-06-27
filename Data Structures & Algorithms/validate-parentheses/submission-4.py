class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map = {"}" : "{", "]" : "[", ")" : "("}
        for c in s:
            if c in hash_map and stack and stack[-1] == hash_map[c]:
                stack.pop()
            else:
                stack.append(c)
            print(stack)
        
        return False if stack else True

        