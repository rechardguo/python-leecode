#https://leetcode-cn.com/problems/rotate-array/
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        nums[:]=nums[-k:]+nums[:-k]

    def roate2(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        for _ in range(k):
            nums.insert(0, nums.pop())

    # 三次反转
    def roate3(self, nums: List[int], k: int) -> None:
        if not nums:
            return
        n = len(nums)
        k %= n
        nums[:] = nums[::-1] # 反转
        nums[:k] = nums[:k][::-1] # 0到k 个反转，k不包括
        print(nums)
        nums[k:] = nums[k:][::-1] # k 到最后个反转
        print(nums)
if __name__ == '__main__':
    l=[1,2,3,4,5,6] # 当作栈来使用
    for i in range(len(l)):
        l.insert(i,l.pop())
        print(l)
    l.append(7) # 插入到最后
    for _ in range(len(l)):
        print(l.pop())
    Solution().roate3(l,3)
    print(l)
