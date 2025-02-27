class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        curr = 0

        for num in nums:
            curr += num
            result.append(curr)

        return result
        