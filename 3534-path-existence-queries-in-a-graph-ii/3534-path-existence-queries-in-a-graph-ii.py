from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # Sort values while keeping original indices
        arr = sorted((nums[i], i) for i in range(n))

        values = [0] * n
        pos = [0] * n

        for i, (value, index) in enumerate(arr):
            values[i] = value
            pos[index] = i

        # Find connected components
        comp = [0] * n
        comp_id = 0
        for i in range(1, n):
            if values[i] - values[i - 1] > maxDiff:
                comp_id += 1
            comp[i] = comp_id

        # Two pointers: furthest reachable in one move
        nxt = [0] * n
        r = 0
        for l in range(n):
            while r + 1 < n and values[r + 1] - values[l] <= maxDiff:
                r += 1
            nxt[l] = r

        # Binary lifting table
        LOG = n.bit_length()
        up = [nxt]

        for _ in range(1, LOG):
            prev = up[-1]
            cur = [0] * n
            for i in range(n):
                cur[i] = prev[prev[i]]
            up.append(cur)

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            left = pos[u]
            right = pos[v]

            if left > right:
                left, right = right, left

            # Different connected components
            if comp[left] != comp[right]:
                ans.append(-1)
                continue

            cur = left
            jumps = 0

            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < right:
                    cur = up[k][cur]
                    jumps += 1 << k

            ans.append(jumps + 1)

        return ans