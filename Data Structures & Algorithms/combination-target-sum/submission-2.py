class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        curr = 0

        def dfs(i, path, curr):
            if curr == target:
                res.append(path.copy())
                return

            if curr > target or i == len(nums):
                return

            path.append(nums[i])
            dfs(i, path, curr + nums[i])

            path.pop()

            dfs(i + 1, path, curr)

        dfs(0, [], curr)

        return res
