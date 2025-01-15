class Solution(object):
    def longestPalindrome(self, s):
        result = ""
        longest = 0

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                temp = s[i:j]
                if temp == temp[::-1]:
                    if len(temp) > longest:
                        longest = len(temp)
                        result = temp
                        
        return result