class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        abs=[]
        for i in range(len(nums)-1):
            for j in range(nums[i]+1, nums[i+1]):
                abs.append(j)
        return abs