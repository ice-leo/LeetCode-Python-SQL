class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        perms = []
        for i, num in enumerate(nums):
            remaining = nums[:i] + nums[i+1:]

            for p in self.permute(remaining):
                perms.append([num] + p)
        return perms
    

        