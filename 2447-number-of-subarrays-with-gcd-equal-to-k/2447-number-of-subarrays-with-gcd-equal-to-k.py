class Solution(object):
    def subarrayGCD(self, nums, k):
        result = 0

        for i in range(len(nums)):
            gcd = nums[i]
            for j in range(i, len(nums)):
                a, b = gcd, nums[j]
                while b:
                    a, b = b, a % b
                gcd = a

                if gcd == k:
                    result += 1
                elif gcd < k:
                    break
        
        return result