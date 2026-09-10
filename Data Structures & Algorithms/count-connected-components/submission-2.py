class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}

        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)

        visited = set()
        res = 0

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for nei in graph[node]:
                dfs(nei)

        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1

        return res