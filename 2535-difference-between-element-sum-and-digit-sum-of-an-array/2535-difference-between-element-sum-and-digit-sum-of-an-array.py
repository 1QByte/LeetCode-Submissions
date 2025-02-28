class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        str_nums = "".join(map(str, nums))
        sumr = 0

        for i in range(len(str_nums)):
            sumr += int(str_nums[i])

        return abs(sum(nums) - sumr)
