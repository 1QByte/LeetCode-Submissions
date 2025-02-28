class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        result = 0

        for sen in sentences:
            temp = sen.count(" ") + 1

            if temp > result:
                result = temp

        return result