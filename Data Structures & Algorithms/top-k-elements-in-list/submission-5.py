class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if not nums:
            return []
        
        count_nums = {}

        for num in nums:
            count_nums[num] = count_nums.get(num, 0) + 1
        
        return [num for num, count in sorted(count_nums.items(), key= lambda x:x[1], reverse=True)][:k]  

        