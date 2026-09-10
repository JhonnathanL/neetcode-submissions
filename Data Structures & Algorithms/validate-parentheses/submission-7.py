class Solution:
    def isValid(self, s: str) -> bool:

        stack = [] 

        chars = {
            ")":"(",
            "]": "[",
            "}": "{"
        }

        for char in s:
            if char in "([{":
                stack.append(char)

            else:
                if not stack or stack[-1] != chars[char]:
                    return False
                    
                stack.pop()

            
        
        return len(stack) == 0
        

