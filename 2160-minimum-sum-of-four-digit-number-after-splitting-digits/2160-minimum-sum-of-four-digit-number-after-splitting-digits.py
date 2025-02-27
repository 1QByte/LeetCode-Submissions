class Solution:
    def minimumSum(self, num: int) -> int:
        nums = sorted(str(num))
        num1 = int(nums[0] + nums[2])
        num2 = int(nums[1] + nums[3])

        return num1 + num2
        