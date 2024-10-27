class Solution:
    def isValid(self, s: str) -> bool:
        brackets_stack = []
        brackets_mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in brackets_mapping.keys():
                # It's a closing bracket
                if not brackets_stack or brackets_stack[-1] != brackets_mapping[char]:
                    return False  # Mismatched or extra closing bracket
                brackets_stack.pop()  # Valid match found
            else:
                # It's an opening bracket
                brackets_stack.append(char)

        return True if len(brackets_stack) == 0 else False  # Return True if all opening brackets are matched