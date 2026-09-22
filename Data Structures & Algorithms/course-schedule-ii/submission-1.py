class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        requisites = {}
        visited = set()
        complete = set()
        valid = []

        for crs, pre in prerequisites:
            if crs not in requisites:
                requisites[crs] = []


            requisites[crs].append(pre)

        def dfs(crs):
            if crs in complete:
                return True

            if requisites.get(crs, []) == []:
                complete.add(crs)
                valid.append(crs)
                return True

            if crs in visited:
                return False

            visited.add(crs)

            for pre in requisites.get(crs, []):
                if not dfs(pre):
                    return False

            visited.remove(crs)

            valid.append(crs)
            complete.add(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return valid