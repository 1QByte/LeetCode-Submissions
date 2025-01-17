class Solution(object):
    def hammingWeight(self, n):
        bin_n = list(bin(n)[2:])

        return bin_n.count("1")
        