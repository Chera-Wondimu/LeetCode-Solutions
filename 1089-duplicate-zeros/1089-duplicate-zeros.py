class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        n = len(arr)
        possible = 0
        last = 0
        while possible < n:
            if arr[last] == 0:
                possible += 2
            else:
                possible += 1
            last += 1
        i = last - 1
        j = n - 1
        if possible > n:
            j = n - 1
            if arr[i] == 0:
                arr[j] = 0
                j -= 1
                i -= 1
        while j >= 0:
            arr[j] = arr[i]
            if arr[i] == 0:
                j -= 1
                if j >= 0:
                    arr[j] = 0
            i -= 1
            j -= 1
        