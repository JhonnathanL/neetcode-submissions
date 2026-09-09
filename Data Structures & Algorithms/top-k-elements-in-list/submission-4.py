class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_numbers = {}

        for number in nums:
            count_numbers[number] = count_numbers.get(number, 0) + 1 

        return [num for num, count in sorted(count_numbers.items(), key=lambda x:x[1], reverse=True)[:k]]   