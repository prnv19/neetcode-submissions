class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok in ["+", "-", "/", "*"]:
                v2 = int(stack.pop())
                v1 = int(stack.pop())
                if tok == "+":
                    stack.append(v1 + v2)
                elif tok == "-":
                    stack.append(v1 - v2)
                elif tok == "*":
                    stack.append(v1 * v2)
                elif tok == "/":
                    stack.append(int(v1/v2))
                continue
            stack.append(int(tok))
        return stack[-1]
        