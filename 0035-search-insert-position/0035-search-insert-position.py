class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if target in nums:
            return nums.index(target)

        else:
            l = 0
            r = len(nums) - 1
            m = (r + l) // 2

            if len(nums) != 2:
                while (m != r) and (m != l):
                    if nums[m] < target:
                        l = m
                        m = (r + l) // 2
                    elif nums[m] > target:
                        r = m
                        m = (r + l) // 2

                if target < nums[l] and target < nums[r]:
                    return 0
                elif target > nums[l] and target > nums[r]:
                    return len(nums)
                elif l == m and target < nums[r]:
                    return m + 1
                else:
                    return m
            else:
                if target < nums[l] and target < nums[r]:
                    return 0
                elif target > nums[l] and target > nums[r]:
                    return len(nums)
                elif target > nums[l] and target < nums[r]:
                    return m + 1
                
            

        