class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def count_letters(word: str):
            seen = {}

            for letter in word:
                if letter not in seen:
                    seen[letter] = 1
                
                else:
                    seen[letter] += 1
                
            return seen

        word1 = count_letters(s)
        word2 = count_letters(t)

        if word1 == word2:
            return True
        
        return False
        
        