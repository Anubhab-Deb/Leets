class Solution:
    def isPalindrome(self, x: int) -> bool:
        arr=list(str(x))

        n=len(arr)

        median=(n-1)//2

        if n%2==0:
            left=median
            right=median+1

        else:
            left=median-1
            right=median+1

        while left>=0 and right<n:
            if arr[left]!=arr[right]:
                return False
            left-=1
            right+=1
        
        return True