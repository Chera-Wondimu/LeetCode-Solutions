class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        ans = 0
        def dfs(node):
            visited.add(node)
            nodes.append(node)
            for i in graph[node]:
                if i not in visited:
                    dfs(i)
        for  j in range(n):
            if j not in visited:
                nodes = []
                dfs(j)
                edge = sum(len(graph[x]) for x in nodes) // 2
                if edge == len(nodes) * (len(nodes) - 1) // 2:
                    ans += 1
        return ans
        