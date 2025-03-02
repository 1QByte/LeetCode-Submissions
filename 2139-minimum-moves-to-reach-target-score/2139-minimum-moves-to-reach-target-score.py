class Solution(object):
    def minMoves(self, target, maxDoubles):
        result = 0

        while target != 1:
            if maxDoubles > 0:
                if target % 2 == 0:
                    target //= 2
                    maxDoubles -= 1
                else:
                    target -= 1
            else:
                return result + (target - 1)

            result += 1

        return result