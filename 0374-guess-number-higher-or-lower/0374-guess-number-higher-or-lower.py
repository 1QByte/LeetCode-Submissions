# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):
# n = 10, pick = 6
class Solution(object):
    def guessNumber(self, n):
        start = 1
        end = n
        
        while start <= end:
            mid = (start + end) // 2
            
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                end = mid - 1
            else:
                start = mid + 1