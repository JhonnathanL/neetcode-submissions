class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        nums = set(nums)     # [2,3,4,5]  3   
        max_sequence = 0

        for num in nums:
            sequence = 0

            if num - 1 not in nums:
                while num + sequence in nums:
                    sequence += 1

                    max_sequence = max(max_sequence, sequence)
        
        return max_sequence
                    