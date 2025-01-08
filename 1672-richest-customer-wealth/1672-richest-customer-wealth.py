class Solution(object):
    def maximumWealth(self, accounts):
        result = []

        for i in accounts:
            result.append(sum(i))
            
        return max(result)