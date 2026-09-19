class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")" : "(", "}" : "{", "]" : "["}
        stack = []

        for c in s:
            print(stack)
            if stack and c in hashmap and stack[-1] == hashmap[c]:
                stack.pop()
                continue
            stack.append(c)
        return True if not stack else False
        