class Solution(object):
    def numIdenticalPairs(self, nums):
        result = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    result += 1
        
        return result