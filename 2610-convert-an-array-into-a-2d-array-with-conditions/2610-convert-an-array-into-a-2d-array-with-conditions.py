class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums_dict = {}
        result = []

        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1

        while any(nums_dict.values()):
            row = []
            for key in list(nums_dict.keys()):
                if nums_dict[key] > 0:
                    row.append(key)
                    nums_dict[key] -= 1
            result.append(row)

        return result
        
        