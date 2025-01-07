class Solution(object):
    def minPartitions(self, n):
        result = []

        for i in n:
            result.append(int(i))
            
        return max(result)
        