class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = ""

        for i in range(len(indices)):
            index = indices.index(i)

            result += s[index]

        return result