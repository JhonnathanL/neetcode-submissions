class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""

        for i in range(len(strs)):
            new_str += str(len(strs[i])) + "#" + strs[i]
        
        return new_str

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # Find the '#'
            while s[j] != "#":
                j += 1

            # Get the length
            length = int(s[i:j])

            # Get the string
            res.append(s[j + 1:j + 1 + length])

            # Move to the next encoded string
            i = j + 1 + length

        return res