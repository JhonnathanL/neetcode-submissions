class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(sub):
            for i in range(len(sub) // 2):
                if sub[i] != sub[-i - 1]:
                    return False
            return True

        def dfs(i, path):
            if i == len(s):
                res.append(path.copy())
                return

            for j in range(i, len(s)):
                sub = s[i:j + 1]

                if is_palindrome(sub):
                    path.append(sub)
                    dfs(j + 1, path)
                    path.pop()

        dfs(0, [])
        return res