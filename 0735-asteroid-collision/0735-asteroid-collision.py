class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if not stack:
                stack.append(ast)
                continue
            
            while True:
                if not stack:
                    stack.append(ast)
                    break
                
                if stack[-1] < 0 and ast < 0 or stack[-1] > 0 and ast > 0:
                    stack.append(ast)
                    break
                if stack[-1] < 0 and ast > 0:
                    stack.append(ast)
                    break
                if abs(stack[-1]) > abs(ast):
                    break
                elif abs(stack[-1]) < abs(ast):
                    stack.pop()
                else:
                    stack.pop()
                    break
        return stack