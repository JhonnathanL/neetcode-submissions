class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        set_nums = set(nums)
        res = 0
        seq = 1

        for n in set_nums:
            if n - 1 not in set_nums:
                seq = 1
                curr = n + 1

                while curr in set_nums:
                    curr+= 1
                    seq+=1
                    
                res = max(res, seq)


        return res
