class Solution:
    
    def merge_sort(self, arr):
        if len(arr)<=1:
            return arr

        mid=len(arr)//2
        left=self.merge_sort(arr[:mid])
        right=self.merge_sort(arr[mid:])

        merged = []
        i=j=0

        while i<len(left) and j<len(right):
            if left[i][0]<right[j][0]:
                merged.append(left[i])
                i+=1
            else:
                merged.append(right[j])
                j+=1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracked=[]
        for i in range(len(nums)):
            tracked.append((nums[i], i))

        tracked=self.merge_sort(tracked)

        x=0
        y=len(tracked)-1

        while x<y:
            curr_sum=tracked[x][0]+tracked[y][0]

            if curr_sum==target:
                return [tracked[x][1], tracked[y][1]]
            elif curr_sum<target:
                x+=1
            elif curr_sum>target:
                y-=1
        return []

    