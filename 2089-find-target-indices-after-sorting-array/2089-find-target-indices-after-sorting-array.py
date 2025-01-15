class Solution(object):
    def targetIndices(self, nums, target):
        nums_sorted = sorted(nums)
        result = []

        for i in range(len(nums_sorted)):
            if nums_sorted[i] == target:
                result.append(i)

        return result