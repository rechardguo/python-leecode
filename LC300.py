# coding=utf-8
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums or len(nums)==0:
            return 0
        maxArr=[1 for i in nums]
        max_incr=1
        for i,v in enumerate(nums):
            for j in range(i):
                if nums[j]<v:
                    maxArr[i]=max(maxArr[i],maxArr[j]+1)
                    max_incr=max(maxArr[i],max_incr)
        return  max_incr