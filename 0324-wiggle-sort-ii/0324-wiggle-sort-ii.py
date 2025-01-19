class Solution(object):
    def wiggleSort(self, nums):
        nums.sort()
        mid = (len(nums) + 1) // 2
        lower = nums[:mid]
        upper = nums[mid:]
        result = []

        i = len(lower) - 1
        j = len(upper) - 1
        
        while i >= 0 or j >= 0:
            if i >= 0:
                result.append(lower[i])
                i -= 1
            if j >= 0:
                result.append(upper[j])
                j -= 1

        nums[:] = result