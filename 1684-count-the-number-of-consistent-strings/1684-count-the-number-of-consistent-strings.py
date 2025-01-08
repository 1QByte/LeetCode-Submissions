class Solution(object):
    def countConsistentStrings(self, allowed, words):
        result = 0

        for word in words:
            if all(char in set(allowed) for char in word):
                result += 1
                
        return result