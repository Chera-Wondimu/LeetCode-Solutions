class Solution:
    def findIntersectionValues(self, nums1, nums2):
        s1 = set(nums1)
        s2 = set(nums2)
        a1 = 0
        a2 = 0
        for x in nums1:
            if x in nums2:
                a1 += 1
        for x in nums2:
            if x in nums1:
                a2 += 1
        return(a1,a2)
       