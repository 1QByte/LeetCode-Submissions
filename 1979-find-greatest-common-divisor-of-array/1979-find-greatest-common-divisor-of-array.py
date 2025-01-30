class Solution(object):
    def findGCD(self, nums):
        smal = min(nums)
        larg = max(nums)

        for i in range(larg, 0, -1):
            if smal % i == 0 and larg % i == 0:
                return i
        