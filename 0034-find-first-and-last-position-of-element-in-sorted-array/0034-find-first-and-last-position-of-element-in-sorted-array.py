class Solution(object):
    def searchRange(self, nums, target):
        first = -1
        last = -1

        for i in range(len(nums)):
            if nums[i] == target:
                if nums.count(target) == 1:
                    first = i
                    last = i
                elif first == -1:
                    first = i
                else:
                    last = i
                    
        return [first, last]