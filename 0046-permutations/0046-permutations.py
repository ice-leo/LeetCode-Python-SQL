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

"""
Mental picture:
[1,2,3]
 ├── 1 + permute([2,3])
 │     ├── 2 + [3]
 │     └── 3 + [2]
 │
 ├── 2 + permute([1,3])
 │     ├── 1 + [3]
 │     └── 3 + [1]
 │
 └── 3 + permute([1,2])
       ├── 1 + [2]
       └── 2 + [1]
"""
    

        
