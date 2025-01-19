class Solution(object):
    def hasAlternatingBits(self, n):
        n_bin = str(bin(n)[2:])
        result = True

        for i in range(len(n_bin) - 1):
            if n_bin[i] == n_bin[i + 1]:
                result = False
                break

        return result
        