class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for number in nums:
            count[number] = count.get(number, 0) + 1

        return [number for number, count in (sorted(count.items(), key=lambda x:x[1], reverse=True)[:k])]
            
