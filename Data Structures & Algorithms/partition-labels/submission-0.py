class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        res = []
        seen = {}

        for i in range(len(s)):
            seen[s[i]] = i
            
        start = 0
        end = 0

        for i in range(len(s)):
            end = max(end, seen[s[i]])

            if i == end:
                res.append(i - start + 1)
                start = i + 1

        return res