class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {}

        for word in strs:
            new_word = "".join(sorted(word))
            if new_word not in res:
                res[new_word] = []
                
            if new_word in res:
                res[new_word].append(word)

        return list(res.values())
