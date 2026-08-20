class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = {}

        for word in strs:
            new_word = "".join(sorted(word))

            if new_word not in seen:
                seen[new_word] = []

            seen[new_word].append(word)
        
        return list(seen.values())