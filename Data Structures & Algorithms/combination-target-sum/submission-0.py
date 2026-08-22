class Solution:
    def combinationSum(self, nums, target):
        res = []

        def backtrack(start, current, total):
            if total == target:
                res.append(current.copy())
                return

            if total > target:
                return

            for i in range(start, len(nums)):
                current.append(nums[i])

                backtrack(i, current, total + nums[i])

                current.pop()

        backtrack(0, [], 0)

        return res