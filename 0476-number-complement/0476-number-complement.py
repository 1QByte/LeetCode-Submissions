class Solution(object):
    def findComplement(self, num):
        binary_list = list(str(bin(num)[2:]))

        for i in range(len(binary_list)):
            if binary_list[i] == "1":
                binary_list[i] = "0"
            else:
                binary_list[i] = "1"
            
        result = int(''.join(binary_list), 2)
        
        return result