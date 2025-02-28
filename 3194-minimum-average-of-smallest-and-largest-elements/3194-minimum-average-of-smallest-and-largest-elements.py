class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        averages = []

        while len(nums) != 0:
            temp = (nums.pop(0) + nums.pop()) / 2
            averages.append(temp)

        return min(averages)

