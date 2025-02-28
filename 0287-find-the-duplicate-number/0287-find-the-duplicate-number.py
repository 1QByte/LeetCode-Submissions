class Solution(object):
    def findDuplicate(self, nums):
        nums_dict = {}
        
        for num in nums:
            if num in nums_dict:
                return num
            else:
                nums_dict[num] = 1
        