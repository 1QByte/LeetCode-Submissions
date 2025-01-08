class Solution(object):
    def smallestEvenMultiple(self, n):
        result = max(n, 2)
    
        while True:
            if result % n == 0 and result % 2 == 0:
                return result
            result += max(n, 2)