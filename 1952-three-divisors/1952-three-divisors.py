class Solution(object):
    def isThree(self, n):
        div = 0

        for i in range(1, n + 1):
            if n % i == 0:
                div += 1

        if div == 3:
            return True
        else:
            return False
        

        