class Solution(object):
    def getSneakyNumbers(self, nums):
        appeared = set()
        duplicates = set()
        
        for i in nums:
            if i in appeared:
                duplicates.add(i)
            else:
                appeared.add(i)
        
        return list(duplicates)