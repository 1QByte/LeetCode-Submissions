class Solution(object):
    def numSteps(self, s):
        result = 0
        s = int(s)

        while s != 1:
            if s % 2 == 0:
                s /= 2
            else:
                s += 1
            result += 1

        return result
        