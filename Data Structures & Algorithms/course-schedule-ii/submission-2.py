class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        requisites = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            requisites[crs].append(pre)

        visited = set()
        complete = []


        def dfs(crs):
            if crs in visited:
                return False

            if crs in complete:
                return True
            
            if requisites[crs] == []:
                complete.append(crs)
                return True

            visited.add(crs)
            
            for pre in requisites[crs]:
                if not dfs(pre):
                    return False
            
            visited.remove(crs)
            complete.append(crs)

            return True


        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return complete
