class Solution(object):
    def findClosestNumber(self, nums):
        result = None
        curr_dictance = abs(nums[0] - 0)
        
        for num in nums:
            if abs(num - 0) < curr_dictance:
                curr_dictance = abs(num - 0)
                result = num
            elif abs(num - 0) == curr_dictance and num > result:
                result = num   

        return result