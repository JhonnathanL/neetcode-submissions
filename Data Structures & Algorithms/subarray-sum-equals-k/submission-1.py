class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix = {0 : 1}  
        curr_sum = 0
        res = 0

        for n in nums:
            curr_sum += n
            diff = curr_sum - k

            if diff in prefix:
                res += prefix[diff]

            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
        
        return res



                




