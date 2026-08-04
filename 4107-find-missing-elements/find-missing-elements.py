class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        abs=[]
        for i in range(nums[0], nums[-1]+1):
            if i not in nums:
                abs.append(i)
        return abs