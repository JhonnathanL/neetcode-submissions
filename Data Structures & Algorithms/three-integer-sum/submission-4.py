class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []

        nums.sort()

        for i, num in enumerate(nums):
            l, r = i + 1, len(nums) - 1

            while l < r:
                curr = num + nums[l] + nums[r]
                seen = [num, nums[l], nums[r]]
                
                if curr == 0 and seen not in res:
                    res.append(seen)
                    l += 1
                    r -= 1

                elif curr < 0:
                    l += 1
                else:
                    r -= 1

        return res
