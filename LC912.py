# https://leetcode-cn.com/problems/sort-an-array/submissions/
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums,0,len(nums)-1)
        return nums

    def quickSort(self,nums,start:int,end:int):
        left=start
        right=end
        if left>right:
            return
        mid=nums[start]
        while left<right:
            while left<right and nums[right]>=mid: #由于有可能重复
                 right-=1
            nums[left]=nums[right]

            while left<right and nums[left]<=mid:
                 left+=1
            nums[right]=nums[left]
        nums[left]=mid;
        # left part
        self.quickSort(nums,start,left-1)
        # right part
        self.quickSort(nums,left+1,end)


if __name__ == '__main__':
    solution=Solution()
    res=solution.sortArray([5,2,3,1])
    for i in res:
     print(i)