class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first=second=0
        for i in nums:
            if i>=first:
                second=first
                first=i
            elif i>second:
                second=i
        return (first-1)*(second-1)