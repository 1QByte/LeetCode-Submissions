class Solution(object):
    def findPermutationDifference(self, s, t):
        result = 0

        for i in range(len(s)):
            result += abs(i - t.find(s[i]))

        return result