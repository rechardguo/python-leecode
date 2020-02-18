from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        mid=self.bs(nums,target,0,len(nums)-1)
        if mid==-1:
            return [-1,-1]
        else:
            left=mid
            tmpLeft=left
            while (tmpLeft:=self.bs(nums,target,0,tmpLeft-1))!=-1:
            left=tmpLeft

        right=mid
        tmpRight=right
        while (tmpRight:=self.bs(nums,target,tmpRight+1,len(nums)-1))!=-1:
        right=tmpRight

    return [left,right]


    def bs(self,nums: List[int], target: int, begin:int ,end:int)->int:
        i=begin
        j=end

        while i<=j:
            mid=(i+j)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                j=mid-1
            else:
                i=mid+1
        return -1