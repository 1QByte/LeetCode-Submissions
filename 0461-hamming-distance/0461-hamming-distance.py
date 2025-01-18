class Solution(object):
    def hammingDistance(self, x, y):
        result = 0
        len_bit = 0

        if x > y:
            len_bit = len(str(bin(x)[2:]))
        else:
            len_bit = len(str(bin(y)[2:]))
            
        x_bin = str(bin(x)[2:].zfill(len_bit))
        y_bin = str(bin(y)[2:].zfill(len_bit))

        for i in range(len(x_bin)):
            if x_bin[i] != y_bin[i]:
                result += 1

        return result
        