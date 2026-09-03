class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        res = []
        visited = set()

        def dfs(i, path):
            if i >= len(nums):
                if tuple(path) not in visited:
                    res.append(path.copy())
                    visited.add(tuple(path))
                
                return
            
            path.append(nums[i])

            dfs(i + 1, path)
            path.pop()
            dfs(i + 1, path)


        dfs(0, [])

        return res