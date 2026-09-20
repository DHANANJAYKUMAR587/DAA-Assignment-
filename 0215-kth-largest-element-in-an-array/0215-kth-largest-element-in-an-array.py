class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        heap=[]
        for i in nums:
            heapq.heappush(heap,i)
        return heapq.nlargest(k,heap)[-1]