#https://leetcode-cn.com/problems/rotate-array/
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums==None or len(nums)==0:
            return
        l=len(nums)
        step=k%l
        def getNext(i:int):
            return (i+step)%l
        i=0
        j=getNext(i)
        last=nums[i]
        while j!=0:
            tmp=nums[j]
            nums[j]=last
            last=tmp
            i=j
            j=getNext(i)
        nums[0]=last
if __name__ == '__main__':
    l=[]
    Solution().rotate(l,3)
    print(l)