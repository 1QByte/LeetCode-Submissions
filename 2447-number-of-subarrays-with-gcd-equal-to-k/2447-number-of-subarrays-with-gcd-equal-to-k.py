class Solution(object):
    def subarrayGCD(self, nums, k):
        result = 0

        for i in range(len(nums)):
            gcd = nums[i]
            for j in range(i, len(nums)):
                while gcd > 0:
                    temp = gcd
                    gcd = nums[j] % gcd
                    nums[j] = temp

                if temp == k:
                    result += 1
                elif temp < k:
                    break
        
        return result

        