class Solution:
    def rob(self, nums: List[int]) -> int:
        
        res = 0
        prev1 = 0
        prev2 = 0

        for n in nums:
            res = max(prev1, prev2 + n)
            prev2 = prev1
            prev1 = res
        
        return res