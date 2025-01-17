class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        result = 0

        for i in range(len(nums)):
            temp = bin(i)[2:]
            if temp.count("1") == k:
                result += nums[i]

        return result
        