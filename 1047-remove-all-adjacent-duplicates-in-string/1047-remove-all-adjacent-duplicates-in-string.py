class Solution:
    def removeDuplicates(self, s: str) -> str:
        letters_stack = []

        for char in s:
            if letters_stack and char == letters_stack[-1]:
                letters_stack.pop()
            else:
                letters_stack.append(char)

        unique_str = ""
        for char in letters_stack:
            unique_str += char

        return unique_str