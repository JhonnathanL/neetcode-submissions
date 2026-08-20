class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for number in nums:
            if number not in count:
                count[number] = 1
            else:
                count[number] += 1

        return [number for number, count in (sorted(count.items(), key=lambda x:x[1], reverse=True)[:k])]
            
