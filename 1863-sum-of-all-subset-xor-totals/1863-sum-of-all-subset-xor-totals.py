class Solution(object):
    def subsetXORSum(self, nums):
        subsets = [[]] 
        result = 0
    
        for num in nums:
            current_subsets = []
            for subset in subsets:
                current_subsets.append(subset + [num])
                
            subsets += current_subsets
        
        for sub in subsets:
            temp = 0
            for i in sub:
                temp ^= i
                
            result += temp

        return result