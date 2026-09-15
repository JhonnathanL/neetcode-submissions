class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
                            
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = i

            complement = target - nums[i]

            if complement in seen and seen[complement] != i:
                return [seen[complement], i]


        return [] 

