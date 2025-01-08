class Solution(object):
    def convertDateToBinary(self, date):
        year, month, day = map(int, date.split('-'))
        
        return bin(year)[2:] + '-' + bin(month)[2:] + '-' + bin(day)[2:]