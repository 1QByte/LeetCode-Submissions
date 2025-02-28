class Solution:
    def countDigits(self, num: int) -> int:
        values = list(map(int, str(num)))
        result = 0

        for val in values:
            if val != 0 and num % val == 0:
                result += 1

        return result