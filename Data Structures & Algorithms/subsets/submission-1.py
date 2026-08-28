class Solution:
    def subsets(self, nums):

        res = []


        def dfs(i, subsets):
            if i == len(nums):
                res.append(subsets.copy())
                return

            subsets.append(nums[i])

            dfs(i + 1, subsets)

            subsets.pop()

            dfs(i + 1, subsets)

        dfs(0, [])

        return res