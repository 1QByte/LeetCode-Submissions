class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = []

        i, j = 0, 1
        while len(nums) != 0:
            arr.append(nums[j])
            arr.append(nums[i])

            nums = nums[2:]
        
        return arr
            