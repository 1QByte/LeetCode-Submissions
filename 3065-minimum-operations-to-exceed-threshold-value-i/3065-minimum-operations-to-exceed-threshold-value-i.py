class Solution(object):
    def minOperations(self, nums, k):
        result = 0

        while nums and min(nums) < k:
            nums.remove(min(nums))
            result += 1
            
        return result