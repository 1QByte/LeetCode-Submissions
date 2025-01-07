class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        result = 0

        for jewel in jewels:
            for stone in stones:
                if jewel == stone:
                    result += 1

        return result
        