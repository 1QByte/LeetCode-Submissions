class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)
        
        if index == -1:
            return word

        result = ""

        for i in range(index, -1, -1):
            result += word[i]
        
        for i in range(index + 1, len(word)):
            result += word[i]

        return result

