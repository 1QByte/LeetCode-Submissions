class Solution(object):
    def countBits(self, n):
        result = []

        for i in range(n + 1):
            temp = str(bin(i)[2:])
            result.append(temp.count("1"))

        return result
        