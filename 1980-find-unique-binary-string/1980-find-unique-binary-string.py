class Solution(object):
    def findDifferentBinaryString(self, nums):
        nums_int = []
        n = len(nums[0])

        for num in nums:
            nums_int.append(int(num, 2))
        
        nums_int.sort()

        for i in range(len(nums_int)):
            if nums[i] != i:
                return bin(i)[2:].zfill(n)
        
        return bin(len(nums))[2:].zfill(n)
