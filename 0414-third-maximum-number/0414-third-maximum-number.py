class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        largest = float("-inf")
        secondlargest = float("-inf")
        thirdMax = float("-inf")

        for num in nums:
            if num == largest or num == secondlargest or num == thirdMax:
                continue

            if num > largest:
                thirdMax = secondlargest
                secondlargest = largest
                largest = num

            elif num > secondlargest:
                thirdMax = secondlargest
                secondlargest = num

            elif num > thirdMax:
                thirdMax = num

        if thirdMax == float("-inf"):
            return largest

        return thirdMax