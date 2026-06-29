class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        prime = [True] * n
        prime[0] = False
        prime[1] = False
        for i in range(2, n):
            if prime[i]:
                j = i * 2
                while j < n:
                    prime[j] = False
                    j += i
        count = 0
        for x in prime:
            if x:
                count += 1
        return count

        