class Solution(object):
    def findErrorNums(self, nums):
        nums_set = set()
        dupl = mis = 0

        for num in nums:
            if num in nums_set:
                dupl = num
            else:
                nums_set.add(num)

        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                mis = i
                break
        
        return [dupl, mis]
        