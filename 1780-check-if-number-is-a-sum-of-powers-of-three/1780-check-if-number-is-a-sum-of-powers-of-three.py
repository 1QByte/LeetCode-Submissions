class Solution(object):
    def checkPowersOfThree(self, n):
        high_pow = 0
        while 3 ** high_pow <= n:
            high_pow += 1

        current_sum = 0
        for power in range(high_pow - 1, -1, -1):
            if current_sum + 3 ** power <= n:
                current_sum += 3 ** power
                
        if current_sum == n:
            return True
        else:
            return False

        
