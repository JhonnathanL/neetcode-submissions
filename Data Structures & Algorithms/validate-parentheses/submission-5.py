class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        valid = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:
            if char in "([{":
                stack.append(char)

            elif stack and valid[char] == stack[-1]:
                stack.pop()
            
            else:
                return False

        return len(stack) == 0
