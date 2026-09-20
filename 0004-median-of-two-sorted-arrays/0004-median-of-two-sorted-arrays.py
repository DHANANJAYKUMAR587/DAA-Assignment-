class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a=nums1+nums2
        b=sorted(a)
        n=len(b)
        if n%2==1:
            return float(b[n//2])
        else:
            return (b[n//2-1]+b[n//2])/2.0