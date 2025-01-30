class Solution(object):
    def gcdOfStrings(self, str1, str2):
        leng = min(len(str1), len(str2))

        for i in range(leng, 0, -1):
            temp = str1[:i]

            if len(str1) % i == 0 and len(str2) % i == 0:
                if temp * (len(str1) // i) == str1 and temp * (len(str2) // i) == str2:
                    return temp
        
        return ""
        