class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        largest=second=0
        for d in str(n):
            d=int(d)
            if d>=largest:
                second=largest
                largest=d
            elif d>second:
                second=d
        return largest*second      