class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []

        i, j = 0, n - 1
        while len(result) != len(nums):
            result.append(nums[i])
            result.append(nums[j])

            i, j = i + 1, j + 1

        return result