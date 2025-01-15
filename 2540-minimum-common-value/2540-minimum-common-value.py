class Solution(object):
    def getCommon(self, nums1, nums2):
        result = list(set(nums1).intersection(set(nums2)))

        if len(result) == 0:
            return -1
        else:
            return min(result)