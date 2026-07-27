class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prod=0
        l=len(nums)
        for i in range(l):
            for j in range(i+1,l):
                prod=max(prod,(nums[i]-1)*(nums[j]-1))
        return prod