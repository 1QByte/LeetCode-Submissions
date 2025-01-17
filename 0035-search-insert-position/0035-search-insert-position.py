class Solution(object):
    def searchInsert(self, nums, target):
        for num in nums:
            if nums == target:
                return nums.index(num)
            else:
                nums.append(target)
                for num in sorted(nums):
                    if num == target:
                        return sorted(nums).index(num)
        