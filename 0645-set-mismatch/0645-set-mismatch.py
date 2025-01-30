class Solution(object):
    def findErrorNums(self, nums):
        nums.sort()
        n = len(nums)
        result = [] 

        for num in nums:
            if nums.count(num) > 1:
                result.append(num)
                nums.remove(num)
                break

        for i in range(1, n + 1):
            if i not in nums:
                result.append(i)
                break
        
        return result
        