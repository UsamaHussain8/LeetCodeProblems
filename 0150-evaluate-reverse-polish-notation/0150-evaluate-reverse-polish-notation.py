class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                ans = op2 + op1
                stack.append(ans)
            elif token == '-':
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                ans = op2 - op1
                stack.append(ans)
            elif token == '*':
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                ans = op2 * op1
                stack.append(ans)
            elif token == '/':
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                ans = op2 / op1
                stack.append(ans)
            else:
                stack.append(token)
            
        return int(stack[-1])
