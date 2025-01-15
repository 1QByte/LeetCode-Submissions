class Solution(object):
    def findDuplicates(self, nums):
        nums_dict = {}
        result = []

        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1

        for key, value in nums_dict.items():
            if value == 2:
                result.append(key)

        return result