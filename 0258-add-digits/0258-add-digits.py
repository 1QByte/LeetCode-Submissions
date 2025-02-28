class Solution:
    def addDigits(self, num: int) -> int:
        result = 0

        while num > 9:
            str_num = str(num)
            temp = 0

            for i in range(len(str_num)):
                temp += int(str_num[i])

            num = temp
            result += 1

        return result
