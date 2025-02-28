class Solution:
    def distinctIntegers(self, n: int) -> int:
        result = {n}

        while n > 1:
            for i in range(2, n):
                if n % i == 1:
                    result.add(i)
            
            n -= 1

        return len(result)