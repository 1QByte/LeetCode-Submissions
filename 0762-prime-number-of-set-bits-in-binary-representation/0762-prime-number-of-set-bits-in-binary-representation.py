class Solution(object):
    def isPrime(self, n):
        if n <= 1:
            return False
        else:
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
                
            return True

    def countPrimeSetBits(self, left, right):
        result = 0
        
        for i in range(left, right + 1):
            temp = bin(i)[2:]
            curr_bit = temp.count("1")
            
            if self.isPrime(curr_bit):
                result += 1
            
        return result
                