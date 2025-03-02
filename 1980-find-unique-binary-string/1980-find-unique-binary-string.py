class Solution(object):
    def findDifferentBinaryString(self, nums):
        nums_int = []
        n = len(nums[0])

        for num in nums:
            nums_int.append(int(num, 2))
        
        for i in range(len(nums_int) + 1):
            if i not in nums_int:
                return bin(i)[2:].zfill(n)
