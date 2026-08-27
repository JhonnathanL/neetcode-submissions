class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        curr_max = nums[0]
        curr_min = nums[0]
        res = nums[0]

        for num in nums[1:]:

            old_max = curr_max

            curr_max = max(
                num,
                num * curr_max,
                num * curr_min
            )

            curr_min = min(
                num,
                num * old_max,
                num * curr_min
            )

            res = max(res, curr_max)

        return res