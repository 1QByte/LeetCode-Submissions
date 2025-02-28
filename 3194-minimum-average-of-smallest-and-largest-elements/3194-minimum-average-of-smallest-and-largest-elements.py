class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        averages = []

        i = len(nums) - 1
        while len(nums) != 0:
            temp = (nums[0] + nums[i]) / 2

            averages.append(temp)
            nums.pop(0)
            nums.pop(i)
            i -= 2

        return sum(averages) / len(averages)

