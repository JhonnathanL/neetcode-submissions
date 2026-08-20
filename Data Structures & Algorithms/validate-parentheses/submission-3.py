class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        paren = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for char in s:
            if char in "([{":
                stack.append(char)
                
            elif stack and paren[char] == stack[-1]:
                stack.pop()
                
            else:
                return False

        return len(stack) == 0              
