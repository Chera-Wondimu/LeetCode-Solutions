class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v in invocations:
            g[u].append(v)
        vis = [0] * n
        def dfs(u):
            vis[u] = 1
            for v in g[u]:
                if not vis[v]:
                    dfs(v)
        dfs(k)
        for u, v in invocations:
            if not vis[u] and vis[v]:
                return list(range(n))
        return [i for i in range(n) if not vis[i]]
        