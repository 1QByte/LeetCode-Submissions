class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            str_num = str(num)
            temp = 0

            for i in range(len(str_num)):
                temp += int(str_num[i])

            num = temp

        return num