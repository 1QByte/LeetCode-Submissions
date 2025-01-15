class Solution(object):
    def countWords(self, words1, words2):
        result = 0

        for word in words1:
            if words1.count(word) == 1 and words2.count(word) == 1:
                result += 1

        return result