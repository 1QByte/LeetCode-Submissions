class Solution(object):
    def getSneakyNumbers(self, nums):
        result = []

        for num in nums:
            if nums.count(num) == 2:
                if num not in result:
                    result.append(num)
                
        return result