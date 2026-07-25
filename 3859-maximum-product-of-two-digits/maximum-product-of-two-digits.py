class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits=[int(d) for d in str(n)] 
        srt=sorted(digits)
        p= srt[-1]*srt[-2] 
        return p