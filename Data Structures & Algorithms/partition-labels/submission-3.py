class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        seen = {}
        res = []

        for i in range(len(s)):
            seen[s[i]] = i

        start = 0
        end = 0
        
        for i in range(len(s)):
            end = max(end, seen[s[i]])
            if end == i:
                res.append(i - start + 1)
                start = i + 1
        
        return res
            
