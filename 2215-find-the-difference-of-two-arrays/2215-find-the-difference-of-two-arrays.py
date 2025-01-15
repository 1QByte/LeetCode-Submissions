class Solution(object):
    def findDifference(self, nums1, nums2):
        result = []

        result.append(list(set(nums1).difference(set(nums2))))
        result.append(list(set(nums2).difference(set(nums1))))

        return result