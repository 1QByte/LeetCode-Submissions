class Solution(object):
    def findKOr(self, nums, k):
        bit_dict = {}
        result = ""
        len_bit = len(str(bin(max(nums))[2:]))

        for num in nums:
            curr_bit = str(bin(num)[2:].zfill(len_bit))
            
            for i in range(len_bit):
                if curr_bit[i] == '1':
                    if i in bit_dict:
                        bit_dict[i] += 1
                    else: 
                        bit_dict[i] = 1
                else:
                    if i in bit_dict:
                        bit_dict[i] += 0
                    else: 
                        bit_dict[i] = 0

        for key, value in bit_dict.items():
            if value >= k:
                result += '1'
            else:
                result += '0'

        return int(result, 2)