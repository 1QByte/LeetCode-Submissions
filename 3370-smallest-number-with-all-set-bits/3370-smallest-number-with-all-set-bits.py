class Solution:
    def smallestNumber(self, n: int) -> int:
        k = len(bin(n)) - 2
        result = (1 << k) - 1
        
        while result < n:
            k += 1
            result = (1 << k) - 1
        
        return result