class Solution:
    def distinctAverages(self, nums):
        nums.sort()
        averages = set()

        while nums:
            avg = (nums.pop(0) + nums.pop()) / 2
            averages.add(avg)

        return len(averages)
