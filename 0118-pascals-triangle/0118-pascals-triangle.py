class Solution(object):
    def generate(self, numRows):
        x = []
        for a in range(numRows):
            row = [1] * (a + 1)
            for b in range(1, a):
                row[b] = x[a - 1][b - 1] + x[a - 1][b]
            x.append(row)
        return x

    

        