class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):

            complement = target - nums[i]

            if complement in seen:
                return [seen[complement], i]
                
            if nums[i] not in seen:
                seen[nums[i]] = i

        return []    