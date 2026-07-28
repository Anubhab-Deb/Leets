class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch, 0)+1
        left=""
        middle=""
        right=""
        for ch in sorted(freq):
            left+=ch*(freq[ch]//2)
            if freq[ch]%2==1:
                middle+=ch
        right=left[::-1]
        return left+middle+right