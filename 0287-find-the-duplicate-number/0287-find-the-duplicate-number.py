class Solution(object):
    def findDuplicate(self, nums):
        nums.sort()
        for num in nums:
            if nums.count(num) > 1:
                return num
        