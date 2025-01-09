class Solution(object):
    def singleNumber(self, nums):
        result = []

        for num in set(nums):
            if nums.count(num) == 1:
                result.append(num)
            
        return result