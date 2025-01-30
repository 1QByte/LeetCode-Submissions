class Solution(object):
    def duplicateNumbersXOR(self, nums):
        nums_dict = {}
        result = 0

        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1

        for key, value in nums_dict.items():
            if value == 2:
                result ^= key

        return result
        