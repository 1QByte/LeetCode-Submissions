class Solution(object):
    def majorityElement(self, nums):
        majority = len(nums) / 2
        nums_dict = {}

        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1

        for key, value in nums_dict.items():
            if value > majority:
                return key
        