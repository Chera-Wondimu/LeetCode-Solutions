
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        tree = [[] for _ in range(n)]
        for i in range(1, n):
            tree[parent[i]].append(i)
        new_tree = [[] for _ in range(n)]
        last = {}
        def dfs(node):
            char = s[node]
            old = last.get(char)
            if old is not None:
                new_tree[old].append(node)
            else:
                new_tree[parent[node]].append(node) if node != 0 else None
            last[char] = node
            for child in tree[node]:
                dfs(child)
            if old is None:
                last.pop(char)
            else:
                last[char] = old
        dfs(0)
        ans = [0] * n
        def calculate(node):
            ans[node] = 1
            for child in new_tree[node]:
                ans[node] += calculate(child)
            return ans[node]
        calculate(0)
        return ans
