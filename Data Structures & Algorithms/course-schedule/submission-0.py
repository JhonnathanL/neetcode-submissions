class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        graph = {}

        for course, prerequisite in prerequisites:
            graph.setdefault(course, []).append(prerequisite)

        visiting = set()
        visited = set()

        def dfs(course):

            if course in visiting:
                return False

            if course in visited:
                return True

            visiting.add(course)

            for prerequisite in graph.get(course, []):
                if not dfs(prerequisite):
                    return False

            visiting.remove(course)
            visited.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True