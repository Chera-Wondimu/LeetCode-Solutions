class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        x = [0] * (2 * n + 2)
        
        def y(index: int, delta: int) -> None:
            while index <= 2 * n + 1:
                x[index] += delta
                index += index & -index
                
        def z(index: int) -> int:
            total = 0
            while index > 0:
                total += x[index]
                index -= index & -index
            return total

        current_sum = n + 1
        y(current_sum, 1)
        total_subarrays = 0
        
        for num in nums:
            current_sum += 1 if num == target else -1
            total_subarrays += z(current_sum - 1)
            y(current_sum, 1)
            
        return total_subarrays