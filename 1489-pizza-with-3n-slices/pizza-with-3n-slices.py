from functools import lru_cache
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        def solve(arr):
            n=len(arr)
            picks=len(slices)//3
            @lru_cache(None)

            def dp(i, k):
                if k==0:
                    return 0
                if i >= n:
                    return float("-inf")
                
                skip=dp(i+1, k)
                take=arr[i] + dp(i+2, k-1)
                return max(skip, take)
            
            return dp(0, picks)

        return max(
            solve(slices[:-1]), 
            solve(slices[1:])
        )