class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        
        nums1 = sorted(nums1 + nums2)
        mid = len(nums1) // 2
        median = 0.0

        if len(nums1) % 2 != 0:
            median = float(nums1[mid])
        else:
            median = (nums1[mid] + nums1[mid - 1]) / 2.0

        return median