class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        requisites = {i : [] for i in range(numCourses)}  
        visited = set()

        for crs, req in prerequisites:
            if crs not in requisites:
                requisites[crs] = []

            requisites[crs].append(req)

        
        def dfs(crs):
            if crs in visited:
                return False
            
            if requisites[crs] == []:
                return True

            visited.add(crs)

            for pre in requisites[crs]:
                if not dfs(pre):
                    return False
            
            visited.remove(crs)
            requisites[crs] = []

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True

