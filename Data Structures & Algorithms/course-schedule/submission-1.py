class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        pre_map = {}
        visited = set()

        for crs, req in prerequisites:

            if crs not in pre_map:
                pre_map[crs] = []
            
            pre_map[crs].append(req)

        def dfs(crs):
            if crs in visited:
                return False
            
            if pre_map.get(crs, []) == []:
                return True
            
            visited.add(crs)

            for pre_req in pre_map.get(crs, []):
                if not dfs(pre_req):
                    return False
            
            visited.remove(crs)
            pre_map[crs] = []

            return True
        
        for crs in list(pre_map.keys()):
            if not dfs(crs):
                return False
        
        return True
        




