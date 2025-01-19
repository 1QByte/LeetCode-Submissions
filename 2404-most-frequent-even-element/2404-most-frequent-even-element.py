class Solution(object):
    def mostFrequentEven(self, nums):
        result = -1
        freq = 0
        nums_dict = {}

        for num in nums:
            if num % 2 == 0:
                if num in nums_dict:
                    nums_dict[num] += 1
                else:
                    nums_dict[num] = 1
                
        for key, value in nums_dict.items():
            if value > freq or (value == freq and key < result):
                result = key
                freq = value
                    
        return result
        