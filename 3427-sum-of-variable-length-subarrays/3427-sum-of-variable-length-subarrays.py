class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        result = nums[0]

        i, j = 0, 1
        while j < n:
            result += (nums[i] + nums[j])
            
            i, j = i + 1, j + 1

        return result
        