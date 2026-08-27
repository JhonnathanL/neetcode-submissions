class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l, r = 0, len(s1)

        list_s1 = sorted(s1)
        count = 0 

        while r < len(s2) + 1:
            if sorted(s2[l:r]) == list_s1:
                return True

            r+=1
            l+=1

        return False


