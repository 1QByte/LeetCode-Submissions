class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        averages = []
        avr_dict = []

        while len(nums) != 0:
            temp = (nums[0] + nums[len(nums) - 1]) / 2

            averages.append(temp)
            nums.pop(0)
            nums.pop()

        for avr in averages:
            if averages.count(avr) > 1:
                avr_dict.append(avr)

        if len(avr_dict) == 0:
            return len(averages)
        else: 
            return len(avr_dict)
