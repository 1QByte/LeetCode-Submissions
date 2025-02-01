class Solution(object):
    def maxCount(self, banned, n, maxSum):
        banned = set(banned)
        result, curr = 0, 0

        for i in range(1, n + 1):
            if i not in banned and curr + i <= maxSum:
                curr += i
                result += 1
            elif curr + i > maxSum:
                break
        
        return result


            
        