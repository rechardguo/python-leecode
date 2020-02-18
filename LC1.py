#https://leetcode-cn.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap={}
        for i in range(0,len(nums)):
            num=target-nums[i]
            if numsMap.get(num) !=None and i!=numsMap.get(num):
                return [numsMap.get(num),i]
            else:
                numsMap[nums[i]]=i