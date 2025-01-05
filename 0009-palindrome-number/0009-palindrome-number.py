class Solution(object):
    def isPalindrome(self, x):
        strX = str(x)
        result = ""

        for i in range(len(strX)-1, -1, -1):
            result += strX[i]

        if strX == result:
            return True
        else:
            return False