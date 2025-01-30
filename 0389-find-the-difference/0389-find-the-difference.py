class Solution(object):
    def findTheDifference(self, s, t):
        for i in t:
            if i in s:
                s = s.replace(i,"")
            else:
                return i
        