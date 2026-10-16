class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = list(map(str, nums))

        arr.sort(key=cmp_to_key(lambda a, b: -1 if a + b > b + a else 1))

        result = ''.join(arr)

        return '0' if result[0] == '0' else result