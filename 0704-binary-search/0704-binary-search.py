
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        m = (l + r) // 2
        
        while nums[m] != target:
            if target in nums[l:m+1]:
                r = m - 1
                m = (l + r) // 2
            elif target in nums[m+1:r+1]:
                l = m + 1
                m = (l + r) // 2
            else:
                return -1
        return m


        