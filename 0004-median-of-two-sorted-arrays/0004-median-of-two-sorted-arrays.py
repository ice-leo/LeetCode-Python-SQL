import numpy as np

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        merged = nums1 + nums2
        sort = sorted(merged)

        l = 0
        r = len(sort) - 1
        m = (l + r)//2

        if len(sort) % 2 == 1:
            return sort[m]
        
        else:
            return (sort[m] + sort[m+1])/2
        