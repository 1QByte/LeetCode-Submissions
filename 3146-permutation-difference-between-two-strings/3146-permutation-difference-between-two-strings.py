class Solution(object):
    def findPermutationDifference(self, s, t):
        result = 0

        for i in range(len(s)):
            temp = t.index(s[i])
            result += abs(i - temp)

        return result
        